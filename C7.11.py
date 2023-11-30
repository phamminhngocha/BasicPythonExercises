# C7.11
# code điều khiển công tắc điện từ xa này chỉ tham khảo.
# Bạn cần có thông tin cụ thể về công tắc điện và tra cứu trong ChatGPT
import RPi.GPIO as GPIO
import time

# Thiết lập chân GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)  # Sử dụng chân GPIO 11

def bat_cong_tac():
    GPIO.output(11, GPIO.HIGH)  # Bật công tắc
    time.sleep(1)  # Giữ công tắc bật trong 1 giây
    GPIO.output(11, GPIO.LOW)  # Tắt công tắc

def tat_cong_tac():
    GPIO.output(11, GPIO.HIGH)  # Bật công tắc
    time.sleep(1)  # Giữ công tắc tắt trong 1 giây
    GPIO.output(11, GPIO.LOW)  # Tắt công tắc

# Sử dụng hàm để bật và tắt công tắc
bat_cong_tac()
time.sleep(2)  # Đợi 2 giây trước khi tắt
tat_cong_tac()

# Dọn dẹp chân GPIO khi kết thúc
GPIO.cleanup()
