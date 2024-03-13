from robotlogger.robotlogger import log_robot_message as _lrm


class RobotLoggerAdapter:
    @staticmethod
    def DEBUG(message):
        _lrm(message, severity=0)

    @staticmethod
    def INFO(message):
        _lrm(message, severity=1)

    @staticmethod
    def WARN(message):
        _lrm(message, severity=2)

    @staticmethod
    def ERROR(message):
        _lrm(message, severity=3)

    @staticmethod
    def CRITICAL(message):
        _lrm(message, severity=4)
