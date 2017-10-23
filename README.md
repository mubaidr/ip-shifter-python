# ip-shifter-python

Command line IP Shifter. Changes IP address from the given address every x seconds.

## How to use

Update config file according to your needs and run `main.py`

## Options

Options are loaded from `config.json` in the root directory.

```json
{
  "ip": {
    "start": "10.50.153.1", /*Starting address of range*/
    "end": "10.50.154.255" /*Ending address of range*/
  },
  "subnet": "255.0.0.0",
  "gateway": "10.50.151.254",
  "dns": "10.50.151.254",
  "timeout": 7, /*Timeout before testing internet on the new IP address*/
  "delay": 50 /*Delay between switching IP addresses*/
}
```
