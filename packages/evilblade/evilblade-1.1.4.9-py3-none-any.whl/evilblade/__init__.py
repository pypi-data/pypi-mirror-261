import os
import subprocess
import sys
from pwn import *
from LibcSearcher import *
import inspect

'''
明知道是陷阱，
    为什么还要来。
'''
RED = '\033[91m'
GREEN = '\033[92m'
END = '\033[0m'
YELLOW = '\033[93m'

n2b = lambda x: str(x).encode()
rv = lambda x: p.recv(x)
rl = lambda: p.recvline()
ru = lambda s: p.recvuntil(s)
sd = lambda s: p.send(s)
sl = lambda s: p.sendline(s)
sn = lambda s: sl(n2b(n))
sa = lambda t, s: p.sendafter(t, s)
sla = lambda t, s: p.sendlineafter(t, s)
sna = lambda t, n: sla(t, n2b(n))
ia = lambda: p.interactive()
rop = lambda r: flat([p64(x) for x in r])
uu64 = lambda data: u64(data.ljust(8, b'\x00'))
rall = lambda : p.recvall()

## Initialize world
def libset(libc_val):
    """
    Set libc for getting offset
    """
    global libc
    libc = ELF(libc_val)

def setup(p_val):
    """
    Set program and start
    """
    global p
    global elf
    p = process(p_val)
    elf = ELF(p_val)

def set(p_val):
    """
    Set program without starting
    """
    global elf
    elf = ELF(p_val)

def rsetup(mip, mport):
    """
    Set up remote connection (remote setup)
    """
    if args.P:
        global p
        p = remote(mip, mport)

## Receive world
def tet():
    """
    Test receiving data for a line 
    """
    p = globals()['p']
    r = ru('\n')
    print('\n----------------\n', 'add', 'is >>> ', r, '\n---------------')
    return r

def getx64(i, j):
    """
    Get 64bit and unpack it with debug info
    """
    if i != 0:
        r = (ru('\n'))[i:j]
        dp('getx64', r)
        r = u64(r.ljust(8, b'\0'))
        print('\n----------------\n', 'add', 'is >>> ', hex(r), '\n---------------')
        return r
    else:
        r = (ru('\n'))[:j]
        dp('getx64', r)
        r = u64(r.ljust(8, b'\0'))
        print('\n----------------\n', 'add', 'is >>> ', hex(r), '\n---------------')
        return r

def getx32(i, j):
    """
    Get 32bit and unpack it with debug info
    """
    if i != 0:
        r = (ru('\n'))[i:j]
        dp('getx32', r)
        r = u32(r.ljust(4, b'\0'))
        print('\n----------------\n', 'add', 'is >>> ', hex(r), '\n---------------')
        return r
    else:
        r = (ru('\n'))[:j]
        dp('getx32', r)
        r = u32(r.ljust(4, b'\0'))
        print('\n----------------\n', 'add', 'is >>> ', hex(r), '\n---------------')
        return r

def getx(i, j):
    """
    Get hex and unpack it with debug info
    """
    if i != 0:
        r = (ru('\n'))[i:j]
        dp('getx', r)
        r = int(r, 16)
        print('\n----------------\n', 'add', 'is >>> ', hex(r), '\n---------------')
        return r
    else:
        r = (ru('\n'))[:j]
        dp('getx', r)
        r = int(r, 16)
        print('\n----------------\n', 'add', 'is >>> ', hex(r), '\n---------------')
        return r

def getd(i, j):
    """
    Get decimal and unpack it with debug info
    """
    if i != 0:
        r = (ru('\n'))[i:j]
        dp('getd', r)
        r = int(r, 10)
        print('\n----------------\n', 'add', 'is >>> ', hex(r), '\n---------------')
        return r
    else:
        r = (ru('\n'))[:j]
        dp('getd', r)
        r = int(r, 10)
        print('\n----------------\n', 'add', 'is >>> ', hex(r), '\n---------------')
        return r

def tryre():
    """
    Try re for check if the connection is still alive
    """
    return p.recvrepeat(2)

def close():
    """
    Close connection
    """
    p.close()

'''
只攻不防，
    天下无双—————
        魔刀千刃。
'''
## Calculate world

def getbase(add, defname, *args):
    """
    Get base from the real address you got
    """
    base = add - libc.symbols[defname]
    for num in args:
        base -= num
    print('\nloading...')
    print('\n----------------\nget!your base is >>> ', hex(base), '\n--------------')
    return base

def evgdb(*argv):
    """
    Set gdb (evil-gdb)
    """
    p = globals()['p']
    context.terminal = ['alacritty', '-e']
    # Modify terminal as per your environment
    # Replace 'alacritty' with the result of running 'echo $TERM'
    if args.G:
        if(len(argv)==0):
            gdb.attach(p)
        else:
            gdb.attach(p, argv[0])

def symoff(defname, *args):
    """
    Calculate or set symblol's offset
    """
    if(len(args)>0):
        ba = args[0]
        print('\n----------------\nyour ', defname, 'offset is >>> ', hex(libc.sym[defname]), '\n---------------')
        print('\n----------------\nyour ', defname, 'is in >>> ', hex(ba+libc.sym[defname]), '\n---------------')
        return libc.sym[defname]+ba
    else:
        print('\n---------------\nyour ', defname, 'offset is >>> ', hex(libc.sym[defname]), '\n---------------')
        return libc.sym[defname]

def gotadd(defname, *args):
    """
    Get got's address
    """
    dpx(f"{defname} got's add", elf.got[defname])
    if (len(args) > 0):
        return elf.got[defname]+args[0]  # Handle PIE
    return elf.got[defname]

def pltadd(defname, *args):
    """
    Get plt's address
    """
    dpx(f"{defname} plt's add", elf.got[defname])
    if (len(args) > 0):
        return elf.plt[defname]+args[0]  # Handle PIE
    return elf.plt[defname]

def symadd(defname, *args):
    """
    Get sym's address
    """
    dpx(f"{defname} sym's add", elf.got[defname])
    if (len(args) > 0):
        return elf.sym[defname]+args[0]  # Handle PIE
    return elf.sym[defname]

def dp(name, data):
    """
    Print data with name
    """
    print('\n---------------\nyour ', name, ' is >>> ', (data), '\n---------------')

def dpx(name, data):
    """
    Print hex data with name
    """
    print('\n---------------\nyour ', name, ' is >>> ', hex(data), '\n---------------')

def d(data):
    """
    Print data without name you input and get name from your local variable
    """
    frame = inspect.currentframe().f_back
    locals_dict = frame.f_locals

    for name, value in locals_dict.items():
        if value is data:
            print('\n---------------\nyour', name, 'is >>>', data, '\n---------------')
            break

def dx(data):
    """
    Hex print data without name you input and get name from your local variable
    """
    frame = inspect.currentframe().f_back
    locals_dict = frame.f_locals

    for name, value in locals_dict.items():
        if value is data:
            print('\n---------------\nyour', name, 'is >>>', hex(data), '\n---------------')
            break

'''
因为，   
    我有想要保护的人。
'''

## Library exploration world

def rlibset(defname, add):
    """
    Set remote libc
    """
    global rlibc
    rlibc = LibcSearcher(defname, add)

def rgetbase(add, defname, *args):
    """
    Get remote libc base from the real address you got
    """
    base = add - rlibc.dump(defname)
    for num in args:
        base -= num
    print('\nloading...')
    print('\n----------------\nget!your base is >>> ', hex(base), '\n--------------')
    return base

def rsymoff(defname, *args):
    """
    Calculate or set remote symblol's offset
    """
    if(len(args)>0):
        ba = args[0]
        print('\n----------------\nyour ', defname, 'offset is >>> ', hex(rlibc.dump(defname)), '\n---------------')
        print('\n----------------\nyour ', defname, 'is in >>> ', hex(ba+rlibc.dump(defname)), '\n---------------')
        return rlibc.dump(defname)+ba
    else:
        print('\n---------------\nyour ', defname, 'offset is >>> ', hex(rlibc.dump(defname)), '\n---------------')
        return rlibc.dump(defname)

# Attack world

def fmt(offset, begin, end, size, written):
    """
    Format string exploit
    """
    payload = fmtstr_payload(offset, {begin: end}, write_size=size, numbwritten=written)
    return payload

'''
    offset（int） - 您控制的第一个格式化程序的偏移量
    字典（dict） - 被写入地址对应->写入的数据，可多个对应{addr: value, addr2: value2}
    numbwritten（int） - printf函数已写入的字节数
    write_size（str） - 必须是byte，short或int。告诉您是否要逐字节写入，短按short或int（hhn，hn或n）
    注意还有ln，lln等用法
'''
def re(time):
    """
    Try to receive
    """
    p.recvS(timeout=time)  # Used for brute-forcing
def clo():
    """
    Close connection
    """
    p.close()

'''
while True:
    ...
    if re:
        print('pwned!get your flag here:', re)
        exit(0)
    p.close()以udi
'''
got = gotadd
plt = pltadd
off = symoff

def execute_script(script_path, mouse=None):
    try:
        # 在脚本文件中插入赋值语句
        if mouse is not None:
            with open(script_path, 'r+') as f:
                content = f.read()
                f.seek(0, 0)
                f.write(f"mouse = {mouse}\n" + content)
        
        # 执行脚本并捕获其输出流和错误流
        process = subprocess.Popen(['python', script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, text=True)
        sleep(0.4)
        output, errors = process.communicate(input='l')  # 传递一个空的输入流
        
        # 获取脚本的退出码
        return_code = process.returncode
        
        # 返回输出流、错误流和退出码
        return output, errors, return_code
    finally:
        # 删除插入的赋值语句
        if mouse is not None:
            with open(script_path, 'r+') as f:
                lines = f.readlines()
                f.seek(0)
                for line in lines:
                    if not line.startswith(f"mouse = {mouse}"):
                        f.write(line)
                f.truncate()

def cyccat():
    """
    get offset of stackoverflow autoly
    """


#仅仅适用于IOT设备，长度过短不会EOF的情况。
def cyccat(your_exp, offset_you_know, overflow_key, large=None, small=None):
    # 初始化 large 和 small
    if large is None:
        large = offset_you_know
    if small is None:
        small = 0

    # 计算 temp，并生成 payload
    temp = (large + small) // 2
    mouse = cyclic(temp)
    
    out, err, return_code = execute_script(your_exp, mouse=mouse)
    d(out)
    d(err)

    if overflow_key == 0:
        # 检查错误
        if "Got EOF" in out:
            # 如果脚本报告EOF错误，则偏移量太大
            print(f"{RED}[-]{END} Offset {temp} too large. Re-adjusting payload...")
            # 更新 large，并递归调用 cyccat
            large = temp // 2
            cyccat(your_exp,offset_you_know, overflow_key, large, small)
        else:
            # 如果没有 EOF 错误，则偏移量太小
            print(f"{RED}[-]{END} Offset {temp} too small. Re-adjusting payload...")
            # 更新 small，并递归调用 cyccat
            small = temp * 2
            cyccat(your_exp,offset_you_know, overflow_key, large, small)

        # 当 large 和 small 相等时，打印找到了
        if large == small:
            print(f"{GREEN}[+]{END} Found the appropriate payload size:{large}")
    else:
        if overflow_key in out:
            # 如果脚本报告EOF错误，则偏移量太大
            print(f"{RED}[-]{END} Offset {temp} too large. Re-adjusting payload...")
            # 更新 large，并递归调用 cyccat
            large = temp // 2
            cyccat(your_exp,offset_you_know, overflow_key, large, small)
        else:
            # 如果没有 EOF 错误，则偏移量太小
            print(f"{RED}[-]{END} Offset {temp} too small. Re-adjusting payload...")
            # 更新 small，并递归调用 cyccat
            small = temp * 2
            cyccat(your_exp,offset_you_know, overflow_key, large, small)

        # 当 large 和 small 相等时，打印找到了
        if large == small:
            print(f"{GREEN}[+]{END} Found the appropriate payload size:{large}")
