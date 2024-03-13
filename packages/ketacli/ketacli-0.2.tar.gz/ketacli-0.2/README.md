# ketadb 工具

示例：

```shell
ketacli login --name <username> --endpoint http://localhost:9000 --token <yourtoken>

ketacli logout

# 枚举所有仪表盘
ketacli list dashboard --fields id,app,updateTime --sort updateTime --order asc --prefix test 

# 描述资源的字段
ketacli describe dashboard 
```
