def mergeSort(ar):
    if len(ar) <= 1:
    	return ar
    mid = len(ar) // 2
    lar = mergeSort(ar[:mid])
    rar = mergeSort(ar[mid:])
    lptr = rptr = arptr = 0
    while lptr < len(lar) or rptr < len(rar):
    	if lptr >= len(lar):
    		ar[arptr] = rar[rptr]
    		rptr += 1
    		arptr += 1
    		continue
    	if rptr >= len(rar):
    		ar[arptr] = lar[lptr]
    		lptr += 1
    		arptr += 1
    		continue
    	if lar[lptr] <= rar[rptr]:
    		ar[arptr] = lar[lptr]
    		arptr += 1
    		lptr += 1
    	else:
    		ar[arptr] = rar[rptr]
    		arptr += 1
    		rptr += 1
    return ar
