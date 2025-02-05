# LedPanelWiFi_HA
Управление [LedPanelWiFi 1.14+](https://github.com/vvip-68/LedPanelWiFi) в Home Assistant

## configuration.yaml

```sh
mqtt:
  binary_sensor: !include_dir_merge_list mqtt/binary
  sensor: !include_dir_merge_list mqtt/sensor
```
