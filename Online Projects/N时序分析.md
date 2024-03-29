
## 概览
时间序列预测相关模型原理及分析思路介绍。

## 模型
### ARIMA模型
Auto Regressive Integrated Moving Average  
https://cloud.tencent.com/developer/article/1646121?areaId=106001  

> 补充阅读：https://jesseyule.github.io/datascience/timeSeries3/content.html

> 关键词：差分，非季节性  
> 参数： p, d, q

- ARIMA是一种基于时间序列历史值和历史值上的预测误差来对当前做预测的模型。
- ARIMA整合了自回归项AR和滑动平均项MA。
- ARIMA可以建模任何存在一定规律的非季节性时间序列。
- 如果时间序列具有季节性，则需要使用SARIMA(Seasonal ARIMA)建模  

> 参数说明  
p - AR(自回归)项的阶数。需要事先设定好，表示y的当前值和前p个历史值有关。   
d - 使序列平稳的最小差分阶数，一般是1阶。非平稳序列可以通过差分来得到平稳序列，但是过度的差分，会导致时间序列失去自相关性，从而失去使用AR项的条件。  
q - MA(滑动平均)项的阶数。需要事先设定好，表示y的当前值和前q个历史值AR预测误差有关。实际是用历史值上的AR项预测误差来建立一个类似归回的模型。  

> When two out of the three terms are zeros, the model may be referred to based on the non-zero parameter, dropping "AR", "I" or "MA" from the acronym describing the model.   
For example, ARIMA(1,0,0)is AR(1), ARIMA(0,1,0) is I(1), and ARIMA(0,0,1) is MA(1).

> ¹²³⁴⁵⁶⁷⁸⁹⁰ , ᵃᵇᶜᵈᵉᶠᵍʰⁱʲᵏˡᵐⁿᵒᵖʳˢᵗᵘᵛʷˣʸᶻ , ₀₁₂₃₄₅₆₇₈₉ , ₐ ₑ ₕ ᵢ ⱼ ₖ ₗ ₘ ₙ ₒ ₚ ᵣ ₛ 
ₜ ᵤ ᵥ ₓ
<!--hidden comment-->

#### 背景介绍
https://jesseyule.github.io/datascience/timeSeries3/content.html   
在AR, MA, ARMA等模型基础上，引入差分法，对不平滑的时间序列数据进行差分计算后转为平滑序列，最后利用普通的ARMA模型建模分析。

1. AR
1. MA
1. ARMA
1. 差分法

#### 模型表示   
1. 完整表示Y<sub>t</sub>：常数+自回归项+滑动平均项 -> c + AR + MA  
即：被预测变量Yt = 常数+Y的p阶滞后的线性组合 + 预测误差的q阶滞后的线性组合
1. 自回归项 - AR项 - auto regression  
p阶的自回归模型可表示为：
    $$y_t = c + \phi_1 y_{t-1} + \phi_2 y_{t-2} + ... + \phi_p y_{t-p} + \epsilon_t $$
    >  c是常数项，ε<sub>t</sub>是随机误差项。  
 对于一个AR(1)模型而言：  
 当 ϕ1=0 时,y<sub>t</sub> 相当于白噪声；  
 当 ϕ1=1 并且 c=0 时,y<sub>t</sub> 相当于随机游走模型；  
 当 ϕ1=1 并且 c≠0 时,y<sub>t</sub> 相当于带漂移的随机游走模型；  
 当 ϕ1<0 时,y<sub>t</sub> 倾向于在正负值之间上下浮动。
1. 滑动平均项 - MA项 - moving average
q阶的预测误差回归模型可表示为：
    $$y_t = c + \epsilon_t + \theta_1 \epsilon_{t-1} + \theta_2 \epsilon_{t-2} + ... + \theta_q \epsilon_{t-q} $$
    > c是常数项，ε<sub>t</sub>是随机误差项。  
 y<sub>t</sub> 可以看成是历史预测误差的加权移动平均值，q指定了历史预测误差的期数。

结合以上，完整表示为：
$$Y_t = c + \Phi_1 Y_{t-1} + \Phi_2 Y_{t-2} + ... + \Phi_p Y_{t-p} + \epsilon^`_t + \Theta_1 \epsilon^`_{t-1} + \Theta_2 \epsilon^`_{t-2} + ... + \Theta_q \epsilon^`_{t-q}$$

#### 模型定阶
1. 自回归AR阶数 - p - pacf图  
通过pacf图来设定，因为AR各项的系数就代表了各项自变量x对因变量y的偏自相关性。
1. 差分阶数 - d - acf图
    - 如果时间序列本身就是平稳的，就不需要差分，所以此时d=0。  
    - 如果时间序列不平稳，那么主要是看时间序列的**acf图**，如果acf表现为10阶或以上的拖尾，那么需要进一步的差分，如果acf表现为1阶截尾，则可能是过度差分了，最好的差分阶数是使acf先拖尾几阶，然后截尾。  
    - 有的时候，可能在2个阶数之间无法确定用哪个，因为acf的表现差不多，那么就选择标准差小的序列。  
1. 滑动平均MA阶数 - q - acf图  
通过acf图来设定，因为MA是预测误差，预测误差是自回归预测和真实值之间的偏差。定阶过程类似AR阶数的设定过程。
1. 信息准则定阶  
信息准则的好处是可以在用模型给出预测之前，就对模型的超参做一个量化评估，这对批量预测的场景尤其有用，因为批量预测往往需要在程序执行过程中自动定阶。
    - AIC(Akaike Information Criterion)
    - AICc（修正过的AIC）
    - BIC(Bayesian Information Criterion)
    > 信息准则越小，说明参数的选择越好，一般使用AICc或者BIC。  
    差分d，不要使用信息准则来判断，因为差分会改变了似然函数使用的数据，使得信息准则的比较失去意义，所以通常用别的方法先选择出合适的d。

#### 模型构建
python:
```  
from statsmodels.tsa.arima_model import ARIMA  
# 1,1,2 ARIMA Model
model = ARIMA(df.value, order=(1,1,2)) 
model_fit = model.fit(disp=0)`  
print(model_fit.summary())
```

#### 检查残差+拟合
通常会检查模型拟合的残差序列，即训练数据原本的序列减去训练数据上的拟合序列后的序列。该序列越符合随机误差分布(均值为0的正态分布)，说明模型拟合的越好，否则，说明还有一些因素模型未能考虑。  

python:  
```
# Plot residual errors
residuals = pd.DataFrame(model_fit.resid)
fig, ax = plt.subplots(1,2)
residuals.plot(title="Residuals", ax=ax[0])
residuals.plot(kind='kde', title='Density', ax=ax[1])
plt.show()

# Actual vs Fitted
model_fit.plot_predict(dynamic=False)
plt.show()
```

#### 模型预测
AUTO ARIMA  
一般可以通过计算AIC或BIC的方式来找出更好的阶数组合。pmdarima模块的`auto_arima`方法就可以让我们指定一个阶数上限和信息准则计算方法，从而找到信息准则最小的阶数组合。

#### 延申
1. 季节性  
如果模型带有季节性，则除了p,d,q以外，模型还需要引入季节性部分$(P,D,Q)_m$：
    $$ARIMA (p,d,q)(P,D,Q)_m$$
    与非季节性模型的区别在于，季节性模型都是以m为固定周期来做计算的，比如D就是季节性差分,是用当前值减去上一个季节周期的值，P和Q和非季节性的p,q的区别也是在于前者是以季节窗口为单位，而后者是连续时间的。
    > 在`auto_arima`方法中，可将seasonal参数设为True，并设置对应的P, D, Q, m参数。  

    > 对于季节性来说，还是用季节性模型来拟合比较合适

1. 引入其他相关变量