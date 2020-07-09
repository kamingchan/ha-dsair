# -*- coding: utf-8 -*-
from enum import Enum, IntEnum

from homeassistant.components.climate.const import \
    HVAC_MODE_COOL, HVAC_MODE_FAN_ONLY, HVAC_MODE_HEAT, HVAC_MODE_DRY, HVAC_MODE_AUTO, HVAC_MODE_HEAT_COOL


class EnumCmdType(IntEnum):
    AIR_CAPABILITY_QUERY = 6
    AIR_CON_CAPABILITY_V2 = 35
    AIR_CON_CLEANING_V = 36
    AIR_RECOMMENDED_INDOOR_TEMP = 4
    AIR_SCENARIO_CONTROL = 32
    CONTROL = 1
    QUERY_SCENARIO_SETTING = 34
    QUERY_STATUS = 3
    SCENARIO_SETTING = 33
    STATUS_CHANGED = 2
    SYS_ACK = 1
    SYS_CHANGE_PW = 17
    SYS_CMD_RSP = 2
    SYS_CMD_TRANSFER = 40961
    SYS_CMD_TRANSFER_TARGET_QUIT = 40962
    SYS_ERR_CODE = 6
    SYS_FILTER_CLEAN_SIGN = 9
    SYS_FILTER_CLEAN_SIGN_RESET = 21
    SYS_GET_ROOM_INFO = 48
    SYS_GET_WEATHER = 7
    SYS_HAND_SHAKE = 40960
    SYS_LOGIN = 16
    SYS_QUERY_SCHEDULE_FINISH = 68
    SYS_QUERY_SCHEDULE = 69
    SYS_QUERY_SCHEDULE_ID = 66
    SYS_QUERY_SCHEDULE_SETTING = 65
    SYS_SCENARIO_CONTROL = 67
    SYS_SCHEDULE_SETTING = 64
    SYS_SET_BASIC_ROOM_INFO = 49
    SYS_TIME_SYNC = 5
    SYS_GET_GW_INFO = 80
    SYS_SET_GW_INFO = 81
    SYS_AUTO_ADDRESS = 82
    SYS_RESTORE_SETTINGS = 83
    SYS_CHECK_NEW_VERSION = 85
    SYS_VERSION_UP_MODE = 86
    SYS_VERSION_UP_STUATUS = 87
    SYS_SET_DISTRIBUTOR_INFO = 88
    SYS_SET_AREA_INFO = 89
    SYS_BIND_OR_UNBIND_SENSOR = 96
    SYS_GET_SENSOR_IN_ROOMS = 98
    SYS_GET_ALL_SENSOR_STATE = 99
    SYS_RESTART = 40963
    SYS_TRANSFER_FAIL = 40964


    SENSOR_INFO =  81
    SENSOR_SET_WARNING_LIMIT = 82
    SENSOR_SET_SLEEP_MODE_TIME = 83
    SENSOR_REMOVE = 84
    SENSOR_R0_RESET = 85
    SENSOR_RESET_INFO = 86
    SENSOR2_R0_RESET = 87
    SENSOR2_RESET_INFO = 88
    SENSOR2_INFO = 89
    SENSOR2_SET_WARNING_LIMIT = 90
    SENSOR2_STATUS = 91
    SENSOR2_CHECK = 92
    SENSOR2_HCHOANDVOC = 93



class EnumDevice(Enum):
    SYSTEM = (0, 0)
    AIRCON = (8, 18)
    GEOTHERMIC = (8, 19)
    VENTILATION = (8, 20)
    HD = (8, 22)
    NEWAIRCON = (8, 23)
    BATHROOM = (8, 24)
    SENSOR = (8, 25)
    IP_MESH_COMMON = (10, 47)
    MESHID_MESH_COMMON = (12, 47)
    IP_LSM = (10, 33)
    MESHID_LSM = (12, 33)
    IP_MESH_SENSOR = (10, 25)
    MESHID_MESH_SENSOR = (12, 25)
    SLEEP_SENSOR = (10, 48)
    IP_RA = (10, 34)
    MESHID_RA = (12, 34)
    SECURITY_MONITOR = (8, 49)



class EnumFanDirection(IntEnum):
    FIX = 0
    STEP_1 = 1
    STEP_2 = 2
    STEP_3 = 3
    STEP_4 = 4
    STEP_5 = 5


class EnumFanVolume(IntEnum):
    NO = 0
    FIX = 1
    STEP_2 = 2
    STEP_3 = 3
    STEP_4 = 4
    STEP_5 = 5
    STEPLESS = 7


class EnumOutDoorRunCond(IntEnum):
    COLD = 2
    HEAT = 1
    VENT = 0


class EnumSwitch(IntEnum):
    ON = 1
    OFF = 2


"""EnumControl"""


class AirFlow(IntEnum):
    SUPER_WEAK = 0
    WEAK = 1
    MIDDLE = 2
    STRONG = 3
    SUPER_STRONG = 4
    AUTO = 5


_AIR_FLOW_NAME_LIST = ['最弱', '稍弱', '中等', '稍强', '最强', '自动']


class Breathe(IntEnum):
    CLOSE = 0
    WEAK = 1
    STRONG = 2

class PRLOprType(IntEnum):
    ADD = 0
    DELETE = 1
    MODIFY = 2

class FanDirection(IntEnum):
    INVALID = 0
    P0 = 1  # 最右 最上
    P1 = 2
    P2 = 3
    P3 = 4
    P4 = 5  # 最左 最下
    AUTO = 6
    SWING = 7


_FAN_DIRECTION_LIST = ['INVALID', '➡️', '↘️', '⬇️', '↙️', '⬅️', '↔️', '🔄']


class Humidity(IntEnum):
    CLOSE = 0
    STEP1 = 1
    STEP2 = 2
    STEP3 = 3

class InfoTemp(IntEnum):
    CONDITION =  1
    HUMIDIFY = 1
    PM25 = 1
    TEMP = 4
    WIND_DIRE = 8
    WIND_SPEED = 16


class Mode(IntEnum):
    COLD = 0
    DRY = 1
    VENTILATION = 2
    AUTO = 3
    HEAT = 4
    AUTODRY = 5
    RELAX = 6
    SLEEP = 7
    PERHEAT = 8
    MOREDRY = 9


_MODE_NAME_LIST = [HVAC_MODE_COOL, 'DRY', HVAC_MODE_FAN_ONLY, 'AUTO', HVAC_MODE_HEAT,
                   HVAC_MODE_DRY, HVAC_MODE_AUTO, HVAC_MODE_HEAT_COOL, 'PERHEAT', 'MOREDRY']


class EnumScenario(Enum):
    BACK_HOME = (1, '回家模式')
    LEAVE_HOME = (0, '离家模式')

class Switch(IntEnum):
    OFF = 0
    ON = 1

class BindState(IntEnum):
    OK = 1
    BINDED_SENSOR = 2
    ON_SENSOR = 5
    OTHER = 2
    UNBINDED_SENSOR = 2

class Type1(IntEnum):
    TEMP = 1
    VOC = 16
    CO2 = 8
    HUMIDITY = 1
    PM25 = 1

class Voc(IntEnum):
    STEP_1 = 1
    STEP_2 = 2
    STEP_3 = 4
    STEP_4 = 8


class Type(IntEnum):
    SWITCH = 1
    MODE = 2
    AIR_FLOW = 4
    FRESH_AIR_HUMIDIFICATION = 8
    SETTED_TEMP = 16
    FAN_DIRECTION = 32
    HUMIDITY = 64
    BREATHE = 128

class FreshAirHumidification(IntEnum):
    OFF = 0
    FRESH_AIR = 5
    HUM_FRESH_AIR = 5

class ThreeDFresh(IntEnum):
    AUTO = 1
    CLOSE = 0
    STRONG = 0 
    WEAK = 1

class TimeType(IntEnum):
    ABSOLUTE = 2
    MONTHLY = 1
    WEEKLY = 0

class EnumControl:
    Switch = Switch
    AirFlow = AirFlow
    Breathe = Breathe
    FanDirection = FanDirection
    Humidity = Humidity
    Mode = Mode
    Type = Type
    FreshAirHumidification = FreshAirHumidification
    ThreeDFresh =  ThreeDFresh

    @staticmethod
    def get_mode_name(idx):
        return _MODE_NAME_LIST[idx]

    @staticmethod
    def get_mode_enum(name):
        return Mode(_MODE_NAME_LIST.index(name))

    @staticmethod
    def get_air_flow_name(idx):
        return _AIR_FLOW_NAME_LIST[idx]

    @staticmethod
    def get_air_flow_enum(name):
        return AirFlow(_AIR_FLOW_NAME_LIST.index(name))

    @staticmethod
    def get_fan_direction_name(idx):
        return _FAN_DIRECTION_LIST[idx]

    @staticmethod
    def get_fan_direction_enum(name):
        return FanDirection(_FAN_DIRECTION_LIST.index(name))
    '''
    @staticmethod
    def get_fresh_air_humidification_name(idx):
        return _FRESH_AIR_HUMIDIFICATION_LIST[idx]

    @staticmethod
    def get_fresh_air_humidification_enum(name):
        return FreshAirHumidification(_FRESH_AIR_HUMIDIFICATION_LIST.index(name))
    '''
