# 浮点数限位（四舍五入）
def Float(a,n=2):
    a = str(a)                                                   # 将浮点数转换为字符串
    b, c, d = a.partition('.')                                   # 将字符串拆成三个部分，整数b，字符串'.',和小数部分d
    e = (d+'0'*n)[:n+1]                                          # 向后补零（防止出现out of range),再截取n位小数
    if len(d)<=n :return float('.'.join([b, e]))                 # 若原小数位数不足n，直接输出
    m = int(d[n])                                                # 取第n+1位小数判断是否需要进位
    if n == 0:                                                   # 考虑四舍五入取整
        if m>= 5:
            return int(b)+1
        else:
            return int(b)
    if m >= 5:                                                   # 考虑“五入”
        L = list(e)                                              # 将e列表化后转化为列表
        L = 0.1**len(e)*int(''.join(L))                          # 将列表合成一个字符串，然后再整型化
        e = str(L+0.1**(len(e)-1))                               # 进位，然后字符串化
        h,i,j = e.partition('.')
        j = (j+'0'*n)[:n]
        if float(e) >= 0.9:                                      # 考虑到进位到整数位的情况
            e = list(e)                                          # 再次列表化e，以删除首位（只有2.9999，或者3.9才会进整）
            del e[0]
            e = ''.join(e)
            b = str(int(b) + 1)
    else:
        e = (d + '0' * n)[:n]
    try:
        e = float('.'.join([b, j]))
    except:
        e = float('.'.join([b, e]))
    return e

# 向上取
def UFloat(a,n=2):
    a = str(a)
    b,c,d = a.partition('.')
    e = (d+'0'*n)[:n]
    e = int(e)+1
    e = str(e)
    if len(e)>n:
        e = list(e)
        e.pop(0)
        e = ''.join(e)
        b = str(int(b)+1)
    return float('.'.join([b, e]))

# 向下取
def DFloat(a,n=2):
    a = str(a)
    b, c, d = a.partition('.')
    e = (d + '0' * n)[:n]
    return float('.'.join([b,e]))
# --------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------矩阵块-------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------

# -------------------------------------------------函数---------------------------------------------------------------
# 矩阵的打印
def Mat_Print(*M):
    for a in M:
        if isinstance(a, list) == True:
            for i in range(len(a)):
                print(a[i])
        else:
            print(a)
    return


# 矩阵的转置
# 得到一个新的矩阵，不改变原矩阵的值
def Mat_Trans(M):
    from copy import deepcopy
    N = deepcopy(M)
    for i in range(len(M)):
        for j in range(len(M)):
            if i<j: [N[i][j], N[j][i]] = [N[j][i], N[i][j]]
    return N



# 矩阵的加法
def Mat_Plus(M,N):
    a = len(M)
    b = len(M[0])
    C = [[0]*a for i in range(a)]
    for i in range(a):
        for j in range(b):
            C[i][j] = M[i][j] + N[i][j]
    return C

# 矩阵的数乘
def Mat_MathMul(n, M):
    from copy import deepcopy
    N = deepcopy(M)
    for i in range(len(M)):
        for j in range(len(M[0])):
            N[i][j] = Float(n*M[i][j],3)
    return N

# 矩阵的乘法
def Mat_Mul(M,N):
    m, n, p, q = len(M[0]), len(M), len(N[0]), len(N)
    if n!=p : return 'Error_Could_Not_Multiply'
    C = [[0]*q for i in range(m)]
    for i in range(m):
        for j in range(q):
            C[i][j]  = sum(M[i][k]*N[k][j] for k in range(n))
    return C

# 余子式
def Mat_Cofact(M, i, j):
    from copy import deepcopy
    N = deepcopy(M)
    for k in range(len(M)):
        del N[k][j]
    del N[i]
    return N

# 行列式
def Mat_Det(M):
    a = len(M)
    b = len(M[0])
    if a != b:return 'could not det'
    Det = 0
    if a==2:
        Det = M[0][0]*M[1][1]-M[0][1]*M[1][0]
    elif a==1:
        Det = M[0][0]
    else:
        Det = sum((-1) ** (i + 1) * M[1][i] * Mat_Det(Mat_Cofact(M, 1, i)) for i in range(a))
    return Det

# 矩阵的伴随
def Mat_Adjugate(M):
    a = len(M)
    C = [[0]*a for i in range(a)]
    for i in range(a):
        for j in range(a):
            C[i][j] = (-1)**(i+j)*Mat_Det(Mat_Cofact(M, i, j))
    return C


# 矩阵的逆
def Mat_Inverse(M):
    if Mat_Det(M) == 0 :return 'Irreversible'
    return Mat_Trans(Mat_MathMul(1/Mat_Det(M), Mat_Adjugate(M)))


# 矩阵的剪切
def Mat_Cut(N,m,n):
    from copy import deepcopy
    M = deepcopy(N)
    a = len(M)
    b = len(M[0])
    if a<m :
        return 'row is not enough to cut'
    if b<n :
        return 'column is not enough to cut'
    else:
        M[m:] = []
        for i in range(m):
            M[i][n:] = []
        return M

# 方阵剪切
def Mat_SquareCut(M):
    from copy import deepcopy
    N = deepcopy(M)
    a = len(M)
    b = len(M[0])
    if a == b:
        return M
    if a<b:
        N = Mat_Cut(M, a, a)
    else:
        N = Mat_Cut(M, b, b)
    return N

# 求方阵的特征多项式
def Mat_Characteristic_Polynomial(M):
    a = len(M)
    x = float()
    from copy import deepcopy
    N = deepcopy(M)
    for i in range(a):
        N[i][i] = M[i][i] - x

# ---------------------------------------------------方法--------------------------------------------------------------

class Mat(list):

    # 矩阵的转置
    # 改变原矩阵的值
    def Trans(N):
        for i in range(len(N)):
            for j in range(len(N)):
                if i < j: [N[i][j], N[j][i]] = [N[j][i], N[i][j]]
        return N


    # 矩阵的数乘
    def MathMul(N, n):
        from copy import deepcopy
        N = deepcopy(N)
        for i in range(len(N)):
            for j in range(len(N[0])):
                N[i][j] = n * N[i][j]
        return N


    # 余子式
    def Cofact(M, i, j):
        from copy import deepcopy
        N = deepcopy(M)
        for k in range(len(M)):
            del N[k][j]
        del N[i]
        return N

    # 行列式
    def Det(M):
        a = len(M)
        b = len(M[0])
        if a != b: return 'could not det'
        Det = 0
        if a == 2:
            Det = M[0][0] * M[1][1] - M[0][1] * M[1][0]
        elif a == 1:
            Det = M[0][0]
        else:
            Det = sum((-1) ** (i + 1) * M[1][i] * M.Cofact(1, i).Det() for i in range(a))
        return Det

    # 矩阵的伴随
    def Adjugate(M):
        a = len(M)
        C = [[0] * a for i in range(a)]
        for i in range(a):
            for j in range(a):
                C[i][j] = (-1) ** (i + j) * M.Cofact(i, j).Det()
        return C

    # 矩阵的逆
    def Inverse(M):
        if M.Det() == 0: return 'Irreversible'
        return Mat(M.Adjugate()).MathMul(1 / M.Det()).Trans()

    # 矩阵的剪切
    def Cut(N, m, n):
        from copy import deepcopy
        M = deepcopy(N)
        a = len(M)
        b = len(M[0])
        if a < m:
            return 'row is not enough to cut'
        if b < n:
            return 'column is not enough to cut'
        else:
            M[m:] = []
            for i in range(m):
                M[i][n:] = []
            return M

    # 方阵剪切
    def SquareCut(M):
        from copy import deepcopy
        N = deepcopy(M)
        a = len(M)
        b = len(M[0])
        if a == b:
            return M
        if a < b:
            N = M.Cut(a, a)
        else:
            N = M.Cut(b, b)
        return N


# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------- 多项式块--------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------- 函数 -----------------------------------------------------------
# 多项式的打印
def Polynomial_Print(*M):
    for a in M:
        if isinstance(a,Polynomial) == True:
            for b in a:
                if b[0] == 0:
                    continue
                elif b == a[0]:
                    print('{}x^{}'.format(b[0],b[1]),end='')
                    continue
                elif b[0]> 0:
                    print('+',end='')
                print('{}x^{}'.format(b[0],b[1]),end='')
        else:
            print(a)
        print('\n')
    return


# 定义多项式的加法
def Polynomial_Plus(A,B):
    from copy import deepcopy
    M = deepcopy(A)
    N = deepcopy(B)
    C = Polynomial(M+N)
    return C.arrange()


# 多项式的乘法
def Polynomial_Mul(M,N):
    m = len(M)
    n = len(N)
    C = Polynomial([[0,i] for i in range(m*n)])
    k = 0
    for i in range(m):
        for j in range(n):
            C[k][0] = M[i][0]*N[j][0]
            C[k][1] = M[i][1]+N[j][1]
            k += 1
    return C.arrange()
# ---------------------------------------------------- 方法 -----------------------------------------------------------

class Polynomial(list):


    # 多项式数乘
    def MathMul(M,n):
        a = len((M))
        C = [[0,i] for i in range(a)]
        for i in range(a):
            C[i][0] = n*M[i][0]
        return C


    # 多项式合并
    def arrange(M):
        m = len(M)
        L = [0]*m
        for i in range(m):
            L[i] = M[i][1]
        L = set(L)
        L = list(L)
        a = len(L)
        N = Polynomial([[0, i] for i in range(a)])
        for i in range(m):
            N[M[i][1]][0] += M[i][0]
        return N

# ---------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------- 我是底线----------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
