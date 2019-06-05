int a[maxN], b[maxN], f[maxN], coef[maxN][maxN];

void mul(int k, int a[maxN], int b[maxN], int c[maxN]) {
  static int ret[maxN + maxN];
  for (int i = 0; i <= k + k - 2; ++i) ret[i] = 0;
  for (int i = 0; i < k; ++i) {
    if (a[i] == 0) continue;
    for (int j = 0; j < k; ++j) {
      ret[i + j] += (LL)a[i] * b[j] % mod;
      ret[i + j] %= mod;
    }
  }
  for (int i = 0; i < k; ++i) c[i] = ret[i];
  for (int i = k; i <= k + k - 2; ++i) {
    if (ret[i] == 0) continue;
    for (int j = 0; j < k; ++j) {
      c[j] += (LL)ret[i] * coef[i - (k - 1)][j] % mod;
      c[j] %= mod;
    }
  }
}

void pow(int k, LL p, int x[maxN], int r[maxN]) {
  static int a[maxN];
  copy(x, x + maxN, a);
  for (int i = 1; i < k; ++i) r[i] = 0;
  r[0] = 1;
  for (; p; p >>= 1) {
    if (p & 1) mul(k, r, a, r);
    mul(k, a, a, a);
  }
}

int solve(int k, int a[maxN], int f[maxN], LL n) { // use f_0, f_n=f_{n-1}*a_1+..+f_{n-k}*a_k
  copy(a + 1, a + 1 + k, b + 1);
  reverse(b, b + 1 + k);
  for (int i = 0; i < k; ++i) coef[1][i] = b[i];
  for (int j = 2; j < k; ++j) {
    coef[j][0] = ((LL)coef[j - 1][k - 1] * b[0]) % mod;
    for (int i = 1; i < k; ++i) {
      coef[j][i] = ((LL)coef[j - 1][k - 1] * b[i] + coef[j - 1][i - 1]) % mod;
    }
  }
  static int ret[maxN];
  fill(ret, ret + maxN, 0); ret[1] = 1;
  int r = 0;
  pow(k, n, ret, ret);
  for (int i = 0; i < k; ++i) {
    r += (LL)ret[i] * f[i] % mod;
    r %= mod;
  }
  return r;
}