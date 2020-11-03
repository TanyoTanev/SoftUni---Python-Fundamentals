'''4. Extract Emails
Write a program to extract all email addresses from a given text. The text comes at the only input line. Print the
emails on the console, each at a separate line. Emails are considered to be in format &lt;user&gt;@&lt;host&gt;, where:
 &lt;user&gt; is a sequence of letters and digits, where &#39;.&#39;, &#39;-&#39; and &#39;_&#39; can appear between them.
o Examples of valid users: &quot;stephan&quot;, &quot;mike03&quot;, &quot;s.johnson&quot;, &quot;st_steward&quot;, &quot;softuni-bulgaria&quot;,
&quot;12345&quot;.
o Examples of invalid users: &#39;&#39;--123&quot;, &quot;.....&quot;, &quot;nakov_-&quot;, &quot;_steve&quot;, &quot;.info&quot;.
 &lt;host&gt; is a sequence of at least two words, separated by dots &#39;.&#39;. Each word is sequence of letters and can
have hyphens &#39;-&#39; between the letters.
o Examples of hosts: &quot;softuni.bg&quot;, &quot;software-university.com&quot;, &quot;intoprogramming.info&quot;,
&quot;mail.softuni.org&quot;.
o Examples of invalid hosts: &quot;helloworld&quot;, &quot;.unknown.soft.&quot;, &quot;invalid-host-&quot;, &quot;invalid-&quot;.
 Examples of valid emails: info@softuni-bulgaria.org, kiki@hotmail.co.uk, no-reply@github.com,
s.peterson@mail.uu.net, info-bg@software-university.software.academy.
 Examples of invalid emails: --123@gmail.com, …@mail.bg, .info@info.info, _steve@yahoo.cn,
mike@helloworld, mike@.unknown.soft., s.johnson@invalid-.
'''
import re
#([a-z]+)(.?)([a-z]*@{1}[a-z]*([.][a-z]*)*)#
pattern = r'([a-zA-Z0-9]+[-\._]*[a-zA-Z0-9]+@[a-zA-Z]+-*[a-zA-Z]+(\.?[a-zA-Z]+-?[a-zA-Z]+)+)'

text = input()#'''Just send email to s.miller@mit.edu and j.hopking@york.ac.uk
#for more information.'''

matches = [x[0] for x in re.findall(pattern, text)]
#matches = re.findall(pattern, text)
#for match in matches:
 # print(match[0])
print("\n".join(matches))