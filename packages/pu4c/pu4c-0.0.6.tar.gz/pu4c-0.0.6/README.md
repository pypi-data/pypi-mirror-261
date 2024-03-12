- A python utils package for city945

- 设计思路
    1. 模块化设计，为每份代码库编写的工具函数汇总作为模块，模块里可以编写特定于该代码库的代码
    2. 面向过程编程，工具函数禁止与数据结构组成类
    3. 模块内文件组织，包含 `utils/common_utils.py` `app.py` `config.py` ，本模块暴露的可被调用的工具函数接口写到 `common_utils.py` 中，应用函数接口写到 `app.py` 中，一些参数配置写到 `config.py` 中，不限制模块间的调用

- 知识点
    - Python 的导包有缓存机制，多次导入与单次导入耗时一致
    - 代码库会生成缓存文件到 `/tmp/pu4c/` 以加速
    - 可以通过 `help(pu4c.pcdet.xxx)` 或 `pu4c.pcdet.xxx.__doc__` 来查看函数注释
