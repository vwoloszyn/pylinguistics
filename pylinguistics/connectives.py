import tools

ConnectiveAdditive = 0




def Additive(pylinguistObj):
    if (pylinguistObj.language == "pt-br"):
    	dic = [tools.clear_string('e'),tools.clear_string('nem'),tools.clear_string('não'),tools.clear_string('só'),tools.clear_string('mas ainda'),\
    	tools.clear_string('além disso'),tools.clear_string('e ainda'),tools.clear_string('também'),tools.clear_string('do mesmo modo'),\
    	tools.clear_string('como ainda'),tools.clear_string('bem como'),tools.clear_string('assim como')]
    	count =0
    	for w in dic:
    		count += clear_string(pylinguistObj.text).count(w)
    global ConnectiveAdditive
    ConnectiveAdditive = count
    return ConnectiveAdditive


def Logic(pylinguistObj):
    if (pylinguistObj.language == "pt-br"):
    	dic = [tools.clear_string('e'),tools.clear_string('nem'),tools.clear_string('não'),tools.clear_string('só'),tools.clear_string('mas ainda'),\
    	tools.clear_string('além disso'),tools.clear_string('e ainda'),tools.clear_string('também'),tools.clear_string('do mesmo modo'),\
    	tools.clear_string('como ainda'),tools.clear_string('bem como'),tools.clear_string('assim como')]
    	count =0
    	for w in dic:
    		count += clear_string(pylinguistObj.text).count(w)
    global ConnectiveAdditive
    ConnectiveAdditive = count
    return ConnectiveAdditive


def Temporal(pylinguistObj):
	### Incidência do operador lógico OU: #Incidência do operador lógico SE em um texto (desconsidera quando o SE é um pronome).
	if (pylinguistObj.language == "pt-br"):
		dic = [tools.clear_string('ou')]
		count =0
		for w in pylinguistObj.tokens:
			if tools.clear_string(w) in dic:
				count+=1
	global LogicOr
	LogicOr = count
	return LogicOr


def Casual(pylinguistObj):
	### Incidência do operador lógico OU: #Incidência do operador lógico SE em um texto (desconsidera quando o SE é um pronome).
	if (pylinguistObj.language == "pt-br"):
		dic = [tools.clear_string('ou')]
		count =0
		for w in pylinguistObj.tokens:
			if tools.clear_string(w) in dic:
				count+=1
	global LogicOr
	LogicOr = count
	return LogicOr




def ConnectiveIncidence(pylinguistObj):
	global LogicNegation
	if (LogicNegation==0):
		LogicNegation = Negation(pylinguistObj)
	return LogicNegation / (float(len(pylinguistObj.postag))/1000)


def AdditiveIncidence(pylinguistObj):
	global LogicIf
	if (LogicIf==0):
		LogicIf = If(pylinguistObj)
	return LogicIf / (float(len(pylinguistObj.postag))/1000)

def LogicIncidence(pylinguistObj):
	global LogicOr
	if (LogicOr==0):
		LogicOr = Or(pylinguistObj)
	return LogicOr / (float(len(pylinguistObj.postag))/1000)

def TemporalIncidence(pylinguistObj):
	global LogicAnd
	if (LogicAnd==0):
		LogicAnd = And(pylinguistObj)
	return LogicAnd / (float(len(pylinguistObj.postag))/1000)

def TemporalIncidence(pylinguistObj):
	global LogicAnd
	if (LogicAnd==0):
		LogicAnd = And(pylinguistObj)
	return LogicAnd / (float(len(pylinguistObj.postag))/1000)

def CasualOperators(pylinguistObj):
	global LogicNegation
	if (LogicNegation==0):
		LogicNegation = Negation(pylinguistObj)
	global LogicIf
	if (LogicIf==0):
		LogicIf = If(pylinguistObj)
	global LogicOr
	if (LogicOr==0):
		LogicOr = Or(pylinguistObj)
	global LogicAnd
	if (LogicAnd==0):
		LogicAnd = And(pylinguistObj)
	
	global LogicAll
	LogicAll = LogicNegation + LogicIf + LogicOr + LogicAnd
	return 	LogicAll


def ConnectiveIncidence(pylinguistObj):
	global LogicAll
	if (LogicAll==0):
		LogicAll = LogicOperators(pylinguistObj)
	return LogicAll / (float(len(pylinguistObj.postag))/1000)

