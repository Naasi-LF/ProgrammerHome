import numpy as np
import matplotlib.pyplot as plt
# 1. 机器精度epsilon的数值是多少？
eps = np.nextafter(1.0, +np.inf) - 1.0
print("epsilon =", eps)

# 2. 验证加2^-52和2^-53
print(1.0 + 2**-52)
print(1.0 + 2**-53)

# 3. 展示 ulp(x)随x变大而变大
xs = [1, 10, 100, 1000, 1e6]
for x in xs:
    ulp = np.nextafter(x, np.inf) - x
    print(f"x={x}, ulp(x)={ulp}")

# 画图展示更多点
X = np.logspace(0, 16, 100)
ULP = np.nextafter(X, np.inf) - X
plt.loglog(X, ULP, label='ulp(x)')
plt.loglog(X, X*eps, '--', label='x*eps')
plt.xlabel('x')
plt.ylabel('ulp(x)')
plt.legend()
plt.title('ulp(x)随x变化的关系')
plt.show()