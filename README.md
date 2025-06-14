# Petrick-s-method
支援 Petrick's method 的核心演算法，
能處理單一布林函數的最小化、理多個布林函數的同步最小化
並找出共享基本質項後總成本最低的 SOP 組合。  
使用 Python 語言與 SymPy 函式庫進行符號運算，確保結果的正確性。 
命令列介面 (CLI)，操作簡單，直觀輸入輸出。
exe 檔可在 [這裡下載](https://drive.google.com/file/d/1Fzu77bznKgMfzZHiTulD3j-THxei-DYz/view?usp=sharing)

## 如何執行
### 環境需求：
Python 3.x
SymPy 函式庫 (pip install sympy)

### 範例使用
以下是一個執行範例，展示了如何輸入數據以及程式的輸出：

#### 範例情境：
假設我們有函數 
f1​=Σm(5,8,9,12,13,14) 和 
f2=Σm(1,3,5,8,9,10)
我們假設基本質項如下：
shared term P1: cover minterms: {5}
shared term P2: cover minterms: {8,9}
f1 獨有 term P3: cover minterms: {5,13}
f1 獨有 term P4: cover minterms: {12,14}
f1 獨有 term P5: cover minterms: {8,9,12,13}
f2 獨有 term P6: cover minterms: {1,3}
f2 獨有 term P7: cover minterms: {1,5}
f2 獨有 term P8: cover minterms: {1,9}
f2 獨有 term P9: cover minterms: {8,10}
會輸出
solution 1 :
  f1's P-function = (P1 & P4 & P5) 
  f1's minimum SOP = (P1 + P4 + P5) 
  f2's P-function = (P1 & P2 & P6 & P9) 
  f2's minimum SOP = (P1 + P2 + P6 + P9) 
 solution 2 :
  f1's P-function = (P1 & P4 & P5) 
  f1's minimum SOP = (P1 + P4 + P5)
  f2's P-function =  (P1 & P6 & P8 & P9)
  f2's minimum SOP =  (P1 + P6 + P8 + P9)
 solution 3 :
  f1's P-function =  (P2 & P3 & P4)
  f1's minimum SOP =  (P2 + P3 + P4)
  f2's P-function =  (P2 & P6 & P7 & P9)
  f2's minimum SOP =  (P2 + P6 + P7 + P9)
  最後按 Enter 就可以關閉
