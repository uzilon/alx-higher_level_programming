 #!/usr/bin/python3
 def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
	return
    best_key: = [x for x in a_dictionary.keys()][0]
    for key in a_dictionary:
	if a_dictionary[best_key] < a_dictionary[key]:
	    best key = key
    return best_key
