d_s, y_s = map(int, input().split())
d_m, y_m = map(int, input().split())
s_year = y_s - d_s
m_year = y_m - d_m

while s_year != m_year:
    if s_year < m_year:
        s_year += y_s
    else: 
        m_year += y_m
print(s_year)