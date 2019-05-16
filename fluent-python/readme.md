# 说明 #
- 《流畅的python》用到的示例全部采用python3.4以上的版本!

# 特殊方法 #
## 1. 跟运算符无关的特殊方法 ##
<table style="BORDER-COLLAPSE: collapse" borderColor=#000000 height=40 cellPadding=1 align=center border=1>
  <tr>
    <th>类别</th>
    <th>方法名</th>
  </tr>
  <tr>
    <th>字符串 / 字节序列表示形式</th>
    <th>__repr__、 __str__、 __format__、 __bytes__</th>
  </tr>
  <tr>
    <th>数值转换</th>
    <th>__abs__、 __bool__、 __complex__、 __int__、 __float__、 __hash__、 __index__</th>
  </tr>
  <tr>
    <th>集合模拟</th>
    <th>__len__、 __getitem__、 __setitem__、 __delitem__、 __contains__</th>
  </tr>
  <tr>
    <th>迭代枚举</th>
    <th>__iter__、 __reversed__、 __next__</th>
  </tr>
  <tr>
    <th>可调用模拟</th>
    <th>__call__</th>
  </tr>
  <tr>
    <th>上下文管理</th>
    <th>__enter__、 __exit__</th>
  </tr>
  <tr>
    <th>实例创建和销毁</th>
    <th>__new__、 __init__、 __del__</th>
  </tr>
  <tr>
    <th>属性管理</th>
    <th>__getattr__、 __getattribute__、 __setattr__、 __delattr__、 __dir__</th>
  </tr>
  <tr>
    <th>属性描述符</th>
    <th>__get__、 __set__、 __delete__</th>
  </tr>
  <tr>
    <th>跟类相关的服务</th>
    <th>__prepare__、 __instancecheck__、 __subclasscheck__</th>
  </tr>
</table>

## 跟运算符相关的特殊方法 ##
<table style="BORDER-COLLAPSE: collapse" borderColor=#000000 height=40 cellPadding=1 align=center border=1>
  <tr>
    <th>类别</th>
    <th>方法名和对应的运算符</th>
  </tr>
  <tr>
    <th>一元运算符</th>
    <th>__neg__ -、 __pos__ +、 __abs__ abs()</th>
  </tr>
  <tr>
    <th>众多比较运算符</th>
    <th>__lt__ <、 __le__ <=、 __eq__ ==、 __ne__ !=、 __gt__ >、 __ge__ >=</th>
  </tr>
  <tr>
    <th>算术运算符</th>
    <th>__add__ +、 __sub__ -、 __mul__ *、 __truediv__ /、 __floordiv__ //、 __mod__ %、 __divmod__ divmod()、 __pow__ ** 或pow()、 __round__ round()</th>
  </tr>
  <tr>
    <th>反向算术运算符</th>
    <th>__radd__、 __rsub__、 __rmul__、 __rtruediv__、 __rfloordiv__、 __rmod__、 __rdivmod__、 __rpow__</th>
  </tr>
  <tr>
    <th>增量赋值算术运算符</th>
    <th>__iadd__、 __isub__、 __imul__、 __itruediv__、 __ifloordiv__、 __imod__、 __ipow__</th>
  </tr>
  <tr>
    <th>位运算符</th>
    <th>__invert__ ~、 __lshift__ <<、 __rshift__ >>、 __and__ &、 __or__ |、 __xor__ ^</th>
  </tr>
  <tr>
    <th>反向位运算符</th>
    <th>__rlshift__、 __rrshift__、 __rand__、 __rxor__、 __ror__</th>
  </tr>
  <tr>
    <th>增量赋值位运算符</th>
    <th>__ilshift__、 __irshift__、 __iand__、 __ixor__、 __ior__</th>
  </tr>
</table>
