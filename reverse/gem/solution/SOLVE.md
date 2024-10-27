# Analysis
1. We start by checking the file type
```bash
main.class: compiled Java class data, version 61.0 (Java SE 17)
```

2. We continue by opening it with `jadx` which is a `java decompiler`
```java
package defpackage;

import org.jruby.Ruby;
import org.jruby.ir.IRScope;
import org.jruby.ir.runtime.IRRuntimeHelpers;

/* compiled from: main.rb */
/* loaded from: main.class */
public class main {
    private static final String script_ir = new StringBuilder().append("������\u0002����\u0003^\u0016\tF��Ut��\u0001'z\u0007salsa20ÿÿÿÿþ\u0010\u0007main.rb��\"\u0001��S\u0001t��\u0001��t����3\u0001F\nUt��\u0003'z\u0011Enter the input: ÿÿÿÿþ\u0010\u0007main.rb\n\"\u0001\u0001S\u0001t��\u0003��t��\u0002F\u000b%\u0003\u0002S����t��\u0004%��\u0003t��\u0004����l\u0004��F\r\"\u0001\u0005S\u0001l\u0004����l\u0006��F\u000f=t��\u0005s\u0007fUt��\u0007'z\bflag.encÿÿÿÿþ\u0010\u0007main.rb\u000fUt��\b'z\u0002wbÿÿÿÿþ\u0010\u0007main.rb\u000f\u0017��\bt��\u0005ÿÿÿÿýt��\u0007t��\bwS\u0002��t��\u0006F\u0013Ut��\n'z$Flag encrypted and saved to flag.encÿÿÿÿþ\u0010\u0007main.rb\u0013\"\u0001\tS\u0001t��\n��t��\t+t��\t\n\u0007requireÿÿÿÿÿ\u0005printÿÿÿÿÿ\u0004getsÿÿÿÿÿ\u0005chompÿÿÿÿÿ\u0005inputÿÿÿÿÿ\fencrypt_flagÿÿÿÿÿ\u000eencrypted_flagÿÿÿÿÿ\u0004Fileÿÿÿÿÿ\u0004openÿÿÿÿÿ\u0004putsÿÿÿÿÿ\u0010\ft����ffR\u0001��fÿÿÿÿÿt����\nl����t������F\u0003Ut��\u0001'z\u0010ftVHDR0k2mLnNhF7ÿÿÿÿþ\u0010\u0007main.rb\u0003Ul\u0001��t��\u0001F\u0004Ut��\u0002'z\u0001��ÿÿÿÿþ\u0010\u0007main.rb\u0004 ��\u0002t��\u0002\u0001f\b��l\u0003��F\u0005=t��\u0003s\u0004f#��\u0005t��\u0003\u0002l\u0001��l\u0003����l\u0006��F\u0006\"��\u0007l\u0006��\u0001l������l\b��F\u0007+l\b��\t\u0005inputÿÿÿÿÿ\u0003keyÿÿÿÿÿ\u0001*ÿÿÿÿÿ\u0005nonceÿÿÿÿÿ\u0007Salsa20ÿÿÿÿÿ\u0003newÿÿÿÿÿ\u0006cipherÿÿÿÿÿ\u0007encryptÿÿÿÿÿ\u000eencrypted_flagÿÿÿÿÿ\f9L\u0015_GLOBAL_ENSURE_BLOCK_��\ft\u0005��\u0001ff\nl����t\u0005��\u0001��F\u0010\"��\u0001l����\u0001l\u0002\u0001��t\u0005\u0001\u0001+t\u0005\u0001\u0001:8L\u0015_GLOBAL_ENSURE_BLOCK_��\u0012t\u0005\u0002\u0001`t\u0005\u0003\u0001\u0002\u0001t\u0005\u0002\u0001.t\u0005\u0003\u00018L\u0007CL1_LBL��\u0003\u0004fileÿÿÿÿÿ\u0005writeÿÿÿÿÿ\u000eencrypted_flagÿÿÿÿÿ\u0003\u0007��\u000b����\u0002\u0005input\u000eencrypted_flagÿÿÿÿÿÿ��������������ÿÿ����?ýffffffffffff��\bÿ����\u00013\u0002\u0002\u0004��\fencrypt_flagÿÿÿÿÿ����\u0005\u0005input\u0003key\u0005nonce\u0006cipher\u000eencrypted_flagÿÿÿÿÿÿ��\u0001����������ÿÿ���� ��ffffffffffff��ÿ����\u0001°ÿ����\u0002P��\u000f\u0004\u0001fÿ��\u0001����������ÿ\ropen &|file|1ÿÿÿÿÿ��\u0001\u0001\u0004fileÿÿÿÿÿÿ��\u0001����������ÿÿ���� ��ffffftffffff��ÿ����\u0002ºÿ����\u00034").toString();

    public static void main(String[] strArr) {
        Ruby newInstance = Ruby.newInstance();
        newInstance.runInterpreter(IRRuntimeHelpers.decodeScopeFromBytes(newInstance, script_ir.getBytes("ISO-8859-1"), "main.rb"));
    }

    public static IRScope loadIR(Ruby ruby, String str) {
        return IRRuntimeHelpers.decodeScopeFromBytes(ruby, script_ir.getBytes("ISO-8859-1"), str);
    }
}
```
3. It uses `jruby` which provides a way to run ruby bytecode inside java
4. We can notice a list of keywords like `encrypt_flag`, `encrypted_flag` and other strings
5. Running `strings` on the file will give us a better idea on the bytecode content
6. A list of symbols are shown but there's some interesting ones like `Salsa20` which is an encryption algorithm
7. We try looking for the `key` using the same way, we'll find another interesting string which has same size as a key `(16 bytes)`: `ftVHDR0k2mLnNhF7`
8. We still need the `nonce`, by looking again at the strings we can find another one with the same size as nonce `(8 bytes)`: `vwAHADYI`

# Solution
```py
from Crypto.Cipher import Salsa20

secret = b'ftVHDR0k2mLnNhF7'

nonce = b'vwAHADYI'

cipher = Salsa20.new(key=secret, nonce=nonce)

with open("flag.enc", "rb") as f:
    cipher_text = f.read()

    flag = cipher.decrypt(cipher_text).decode()

    print(flag)
```

# Flag
`shellmates{5aL54_20_1N_rU8y}`