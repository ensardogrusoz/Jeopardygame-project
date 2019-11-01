export SECRET_KEY="35ffde6edaf0b45ca8cec399edb31424ea88abf06cc04adc"
export DEBUG_VALUE="True"

for file in ~/.{bash_prompt, aliases, private}; do
	[ -r "$file" ] && [ -f "$file" ] && source "$file";
done;