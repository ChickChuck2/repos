from cuesdk import CueSdk
from cuesdk.enums import CorsairLedId



def __init__():
    sdk = CueSdk()
    sdk.connect()

    print(sdk.protocol_details)
    print(sdk.get_devices())

    sdk.set_led_colors_flush_buffer()

if __name__ == "__main__":
    __init__()