import logging
import socket
import time
import types
import typing
from threading import Thread, Lock

from .ctrl_enum import EnumDevice
from .dao import Room, AirCon, AirConStatus, get_device_by_aircon
from .decoder import decoder, BaseResult
from .display import display
from .param import Param, HandShakeParam, HeartbeatParam, AirConControlParam, AirConQueryStatusParam

_LOGGER = logging.getLogger(__name__)


def _log(s: str):
    for i in s.split('\n'):
        _LOGGER.debug(i)


class SocketClient:
    def __init__(self, host: str, port: int):
        self._host = host
        self._port = port
        self._locker = Lock()
        self._s = None
        while not self.do_connect():
            time.sleep(3)
        self._recv_thread = RecvThread(self)
        self._recv_thread.start()

    def do_connect(self):
        self._s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self._s.connect((self._host, self._port))
            return True
        except Exception:
            return False

    def send(self, p: Param):
        self._locker.acquire()
        _log('send:')
        _log(display(p))
        done = False
        while not done:
            try:
                self._s.sendall(p.to_string())
                done = True
            except Exception as e:
                print ("send false:", e)
                time.sleep(3)
                self.do_connect()
        self._locker.release()

    def recv(self) -> typing.List[BaseResult]:
        res = []
        done = False
        data = None

        while not done:
            try:
                data = self._s.recv(1024)
                done = True
            except Exception:
                time.sleep(3)
                self.do_connect()
        while data:
            r, b = decoder(data)
            res.append(r)
            data = b
        return res


class RecvThread(Thread):
    def __init__(self, sock: SocketClient):
        super().__init__()
        self._sock = sock
        self._locker = Lock()

    def run(self) -> None:
        while True:
            res = self._sock.recv()
            for i in res:
                _log('recv:')
                _log(display(i))
               # print ('recv:',display(i))
                if i is None:
                    continue
                self._locker.acquire()
                i.do()
                self._locker.release()


class HeartBeatThread(Thread):
    def __init__(self, service):
        super().__init__()
        self.service = service

    def run(self) -> None:
        super().run()
        time.sleep(30)
        cnt = 0
        while True:
            self.service.send_msg(HeartbeatParam())
            cnt += 1
            if cnt == 5:
                cnt = 0
                self.service.poll_aircon_status()
            time.sleep(60)


class Service:
    _socket_client = None  # type: SocketClient
    _rooms = None  # type: typing.List[Room]
    _aircons = None  # type: typing.List[AirCon]
    _new_aircons = None  # type: typing.List[AirCon]
    _ventilation = None
    _sensor = None
    _bathrooms = None  # type: typing.List[AirCon]
    _ready = False  # type: bool
    _none_stat_dev_cnt = 0  # type: int
    _status_hook = []  # type: typing.List[(AirCon, types.FunctionType)]
    _heartbeat_thread = None

    def __init__(self, host: str, port: int):
        self._socket_client = SocketClient(host, port)
        self._socket_client.send(HandShakeParam())
        self._heartbeat_thread = HeartBeatThread(self)
        self._heartbeat_thread.start()
        while self._rooms is None or self._aircons is None \
                or self._new_aircons is None or self._bathrooms is None:
            time.sleep(1)
        for i in self._aircons:
            for j in self._rooms:
                if i.room_id == j.id:
                    i.alias = j.alias
                    if i.unit_id:
                        i.alias += str(i.unit_id)
        for i in self._new_aircons:
            for j in self._rooms:
                if i.room_id == j.id:
                    i.alias = j.alias
                    if i.unit_id:
                        i.alias += str(i.unit_id)
        for i in self._bathrooms:
            for j in self._rooms:
                if i.room_id == j.id:
                    i.alias = j.alias
                    if i.unit_id:
                        i.alias += str(i.unit_id)
        self._ready = True


    def get_aircons(self):
        return self._aircons

    def get_new_aircons(self):
        return self._new_aircons

    def get_ventilation(self):
        return self._ventilation

    def get_sensor(self):
        return self._sensor

    def control(self, aircon: AirCon, status: AirConStatus):
        p = AirConControlParam(aircon, status)
        self.send_msg(p)

    def register_status_hook(self, device: AirCon, hook):
        self._status_hook.append((device, hook))

    # ----split line---- above for component, below for inner call

    def is_ready(self) -> bool:
        return self._ready

    def send_msg(self, p: Param):
        """send msg to climate gateway"""
        self._socket_client.send(p)

    def get_rooms(self):
        return self._rooms

    def set_rooms(self, v: typing.List[Room]):
        self._rooms = v

    def set_device(self, t: EnumDevice, v: typing.List[AirCon]):
        self._none_stat_dev_cnt += len(v)
        if t == EnumDevice.AIRCON:
            self._aircons = v
        elif t == EnumDevice.NEWAIRCON:
            self._new_aircons = v
        else:
            self._bathrooms = v

    def set_aircon_status(self, target: EnumDevice, room: int, unit: int, status: AirConStatus):
        if self._ready:
            self.update_aircon(target, room, unit, status=status)
        else:
            li = []
            if target == EnumDevice.AIRCON:
                li = self._aircons
            elif target == EnumDevice.NEWAIRCON:
                li = self._new_aircons
            elif target == EnumDevice.BATHROOM:
                li = self._bathrooms
            for i in li:
                if i.unit_id == unit and i.room_id == room:
                    i.status = status
                    self._none_stat_dev_cnt -= 1
                    break

    def poll_aircon_status(self):
        for i in self._new_aircons:
            p = AirConQueryStatusParam()
            p.target = EnumDevice.NEWAIRCON
            p.device = i
            self.send_msg(p)

    def update_aircon(self, target: EnumDevice, room: int, unit: int, **kwargs):
        li = self._status_hook
        for item in li:
            i, func = item
            if i.unit_id == unit and i.room_id == room and get_device_by_aircon(i) == target:
                try:
                    func(**kwargs)
                except Exception as e:
                    _log('hook error!!')
                    _log(str(e))
