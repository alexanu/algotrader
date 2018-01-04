
from view import price_to_string, heartbeat_to_string, price_to_string2
from common.config import OandaContext
import json

def main():
    """
    Stream the prices for a list of Instruments for the active Account.
    """
    show_heartbeats = False

    # Create empty context
    ctx = OandaContext('demo')
    # Load configuration
    ctx.load_configuration()
    # Create API
    api = ctx.create_streaming_context()


    account_id = ctx.active_account
    #api.set_convert_decimal_number_to_native(False)
    #api.set_stream_timeout(3)

    
    # Subscribe to the pricing stream
    response = api.pricing.stream(account_id,
                                  instruments="EUR_USD,USD_CAD")
                            
    #print(response)

    
    
    # Print out each price as it is received
    for msg_type, msg in response.parts():
        if msg_type == "pricing.Heartbeat" and show_heartbeats:
            print(heartbeat_to_string(msg))
        elif msg_type == "pricing.Price":
            print(price_to_string2(msg))


if __name__ == "__main__":
    main()
