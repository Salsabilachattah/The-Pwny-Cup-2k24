# Analysis
1. By doing a simple search about the assembly syntax we'll find it's an interepreted programming language bytecode disassemble
2. Looking fore more details we'll guide us to find that it's a `Lua` bytecode disassemble
3. We can either try to do static analysis and understand the code by reading it or try something like asking from `ChatGPT` or any similar service to reconstruct the high level language to understand more fast
```lua
local function Combine(target, source)
    for i = 1, #source do
        table.insert(target, source[i])
    end
end

local function Enc1(data)
    local result = {}
    for i = 1, #data do
        local char = data:sub(i, i)
        table.insert(result, (char:byte() + 3) % 256)
    end
    return result
end

local function Enc2(data)
    local result = {}
    for i = 1, #data do
        local char = data:sub(i, i)
        table.insert(result, (char:byte() - 3) % 256)
    end
    return result
end

local function Enc3(data)
    local result = {}
    for i = 1, #data do
        local char = data:sub(i, i)
        table.insert(result, (char:byte() + 6) % 256)
    end
    return result
end

local function Enc4(data)
    local result = {}
    for i = 1, #data do
        local char = data:sub(i, i)
        table.insert(result, (char:byte() - 6) % 256)
    end
    return result
end

io.write("Enter flag: ")
local flag = io.read()
if #flag ~= 40 then
    print("Wrong")
else
    local combined = {}
    Combine(combined, Enc2(flag:sub(1, 10)))
    Combine(combined, Enc1(flag:sub(11, 20)))
    Combine(combined, Enc4(flag:sub(21, 30)))
    Combine(combined, Enc3(flag:sub(31, 40)))

    local result = table.concat(combined, ",")
    if result == "112,101,98,105,105,106,94,113,98,112,126,79,120,55,98,101,92,98,117,51,50,45,108,78,42,89,70,45,108,111,59,58,82,111,115,59,73,78,127,131" then
        print("Correct")
    else
        print("Wrong")
    end
end
```

# Solution
```python
def dec1(chunk):
    return [chr((ord(x) - 3) % 256) for x in chunk]

def dec2(chunk):
    return [chr((ord(x) + 3) % 256) for x in chunk]

def dec3(chunk):
    return [chr((ord(x) - 6) % 256) for x in chunk]

def dec4(chunk):
    return [chr((ord(x) + 6) % 256) for x in chunk]

enc_flag = "".join([chr(int(x)) for x in "112,101,98,105,105,106,94,113,98,112,126,79,120,55,98,101,92,98,117,51,50,45,108,78,42,89,70,45,108,111,59,58,82,111,115,59,73,78,127,131".split(",")])

flag = "".join(
    dec2(enc_flag[0:10]) + 
    dec1(enc_flag[10:20]) +
    dec4(enc_flag[20:30]) +
    dec3(enc_flag[30:40])
)

print(flag)
```

# Flag
`shellmates{Lu4_bY_r083rT0_L3ru54Lim5CHy}`