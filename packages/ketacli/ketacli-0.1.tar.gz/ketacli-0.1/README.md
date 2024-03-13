# ketadb 工具

示例：

```shell
ketacli login --name <username> --endpoint http://localhost:9000 --token <yourtoken>

ketacli logout

# 枚举所有仪表盘
ketacli.py list dashboard --fields id,app,updateTime --sort updateTime --order asc --prefix test 
```
