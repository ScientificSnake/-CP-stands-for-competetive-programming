import sys

sys.stdin = open("censor.in", 'r')
sys.stdout = open("censor.out", "w")
text = input()
badText = input()

badTextLen = len(badText)

# while True:
#     pre, sep, suff = text.partition(badText)
#     if sep != '':
#         text = pre + suff
#     else:
#         break
# print(text)

censored = ""
# Add each character to the censored string
for char in text:
	censored += char
	# If the end of the string is t, we remove t from the end
	if censored[-len(badText) :] == badText:
		censored = censored[: -len(badText)]

print(censored)