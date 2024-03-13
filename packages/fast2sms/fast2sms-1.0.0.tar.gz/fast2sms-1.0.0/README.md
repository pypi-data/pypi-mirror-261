# Fast2 SMS

> Python package for [FAST2 SMS](https://www.fast2sms.com) API Client

## Client setup

```python

from fast2sms import F2Client

# Initialize The Client 
f2 = F2Client(api_key="YOUR_API_KEY")


response = f2.quick_sms(
    numbers="999999999, 1111111111, 8888888888", # You can use multiple number split with coma 
    msg="Hey This Is Test Message",
)

print(response.text) # return is json value 

```

## Installing
```
pip install fast2sms
```

## Dependencies

• requests

• Python 3+


### Support

- [MR MKN](https://github.com/MrMKN)
- [Telegram](https://t.me/mkn_bots_updates)
