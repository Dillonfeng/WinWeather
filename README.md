# WinWeather · 老黄历

一个单文件的 Windows 桌面日历：`老黄历.hta`，双击即可运行，无需安装任何运行环境。

## 运行

双击 `老黄历.hta`，或在命令行执行：

```
mshta.exe "老黄历.hta"
```

首次运行会在同目录生成 `holidays.txt`、`school.txt`、`myfest.txt`、`huangli_cfg.json` 与 `images/` 目录；自动定位时临时生成 `hl_geoloc.ps1`（Windows 定位辅助脚本）与 `hl_geo.txt`（定位结果，读后即删）。

> **和风天气 API Key**：程序启动时会读取同目录 `huangli_cfg.json` 中的 `qweatherKey` 字段。
> 有 key 时，天气/空气质量/紫外线/气象预警/台风全部走和风单一源；
> 无 key 时自动降级为 weather.com.cn + wttr.in + typhoon.nmc.cn。
> `huangli_cfg.json` 已在 `.gitignore` 中，不会提交到公开仓库。

## 功能

| 模块 | 说明 |
|---|---|
| 黄历 | 农历、干支、生肖、宜忌、值神、冲煞、节气、传统节日 |
| 月相 | 按农历日推算 8 相，盈亮面在右、亏亮面在左；日行首尾标注「开始/结束」 |
| 万年历 | 整月网格，支持**周一开头 / 周日开头**切换 |
| 天气 | 和风天气 6 接口：实况 / 7 天预报 / 实时 AQI / 5 天 AQI 预报 / 紫外线 / 气象预警 |
| 空气质量 | 当前 AQI + 未来 5 天（今天用实时实测、未来用预报预测）；悬停看 PM2.5 / PM10 |
| 气象预警 | 和风 weatheralert 覆盖台风 / 高温 / 暴雨 / 大风 / 雷电 / 寒潮 / 沙尘暴 / 大雾 / 霾 / 干旱 / 冰雹 等 |
| 台风 | 和风 tropical-cyclone 全球活跃台风跟踪（位置 / 强度 / 风速 / 气压 / 移向移速 / 64 节风圈）；nmc 兜底 |
| 节日海报 | 自动搜图；节日/生日配图不理想时可在设置里指定图片来源 |
| 调休同步 | 每天自动从接口同步国务院放假与调休安排 |
| 跨天刷新 | 零点后自动翻到新的一天，无需重启 |

## 设置

点右上角 ⚙ 打开：

- **城市** —— 首次启动自动定位到县区级；定位链路：Windows WiFi/GPS + ip-api IP 坐标并行，坐标出来后经和风 GeoAPI 反查区县（如「深圳南山」）。设置里可手动「重新定位」
- **每周** —— 周一开头 / 周日开头
- **开机** —— 登录后自动启动（写入 `HKCU Run`，无需管理员权限）
- **学校** —— 深圳中小学寒暑假与春秋假
- **自定义节日** —— 支持每年公历 / 每年农历 / 仅一次，可配弹窗文字与配图来源

## 数据来源（优先级从高到低）

| 数据 | 主要来源 | 降级兜底 |
|---|---|---|
| 实况天气（温/湿/风/气压/能见度/体感） | 和风 `/v7/weather/now` | weather.com.cn + wttr.in |
| 7 天预报 | 和风 `/v7/weather/7d` | weather.com.cn |
| 实时 AQI / PM2.5 / PM10 | 和风 `/airquality/v1/current` | sojson |
| 5 天 AQI 预报 | 和风 `/airquality/v1/daily` | sojson 15 天 AQI 截取 |
| 紫外线 | 和风 `/v7/indices/1d?type=5` | wttr.in |
| 气象预警（高温/暴雨/大风/…） | 和风 `/weatheralert/v1/current` | — |
| 台风跟踪（活跃台风 + 实况） | 和风 `/v7/tropical/storm-list` + `storm-track` | 中国气象局台风网 `typhoon.nmc.cn` |
| 本地台风预警 | 和风 `/weatheralert/v1/current`（事件码 1001） | — |
| 节假日 | timor.tech | — |
| IP 定位 | ip-api.com + ipip.net | — |

## 自定义节日配图

在设置里为节日填写「配图」，支持三种方式，优先级从高到低：

1. **本地图片** —— 把图片放进 `images/`，文件名与「配图」栏一致即可（支持 jpg/jpeg/png/gif/bmp）
2. **图片网址** —— 填 `http(s)://...`，直接使用，不联网搜索
3. **搜索关键词** —— 填 `姓名 男士` 之类，用它去搜图

留空则按节日名自动搜索。

## 浏览器内核说明

本程序依赖 IE9 文档模式运行（`<meta http-equiv="X-UA-Compatible" content="IE=9">`），
但请求接口已全部升级为 HTTPS；表格行不能直接赋 `innerHTML`，需用
`insertRow()/insertCell()` 构建。
