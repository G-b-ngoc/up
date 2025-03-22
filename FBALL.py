p = float(input())
q = float(input())
r = float(input())
s = float(input())
u = float(input())
v = float(input())
ur = p and q and r and s and u and v
def bien(x):
    if p and q and r and s and u <= 20:
      return True
if ur >1:
    x = p * 3
    y = q * 0
    a = x+ y

    x = r * 3 
    y = s * 0
    b = x+ y

    x = u * 3 
    y = v * 0
    z = x+ y

print(f"{int(a)} {int(b)} {int(z)}")