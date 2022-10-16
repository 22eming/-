func solution(s string) bool { 
    if (!(len(s) == 4 || len(s) == 6)) {
		return false
	}

	for _, value := range s {
		if value < '0' || value > '9' {
			return false
		} 
	}

	return true
}