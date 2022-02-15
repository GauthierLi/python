import numpy as np
import logging

# 默认输入等级是warning
fmt = "%(name)s--->%(message)s--->%(asctime)s" # 时间格式器 
logging.basicConfig(level="DEBUG", format=fmt)
logging.debug("debug information")
logging.info("info information")
logging.warning("warning information")
logging.error("error information")
logging.critical("cri information")


