import re;

regex = re.compile("[a-z]* [a-z]* [a-z]*");
val = "park sung cheol[11]";
searched = regex.search(val);
matched = regex.match(val);

print(searched, matched.group());

print(val.replace(matched.group(), "kim ji hoon"));
