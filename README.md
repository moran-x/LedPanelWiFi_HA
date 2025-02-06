# LedPanelWiFi_HA
Управление [LedPanelWiFi 1.14+](https://github.com/vvip-68/LedPanelWiFi) в Home Assistant

## configuration.yaml

```sh
mqtt:
  light: !include_dir_merge_list mqtt/light
  switch: !include_dir_merge_list mqtt/switch
  sensor: !include_dir_merge_list mqtt/sensor
```
