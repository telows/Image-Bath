
//may remake dhash in cpp for speed
/*
	source:
	http://www.hackerfactor.com/blog/index.php?/archives/529-Kind-of-Like-That.html

	1. reduce img size to 9x8 = 72 pixels
	2. convert to grayscale 
	(may need do do first or similtaniously with size reduction)
	3. compute difference in adjacent pixels
	4. assign bits based on left being brighter than right

*/