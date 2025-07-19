def calculate_mn(data):
    total_ni_mi = sum(Ni * Mi for Ni, Mi in data)
    total_ni = sum(Ni for Ni, _ in data)
    return total_ni_mi / total_ni if total_ni else 0

def calculate_mw(data):
    total_ni_mi2 = sum(Ni * (Mi ** 2) for Ni, Mi in data)
    total_ni_mi = sum(Ni * Mi for Ni, Mi in data)
    return total_ni_mi2 / total_ni_mi if total_ni_mi else 0

def calculate_pdi(mn, mw):
    return mw / mn if mn else 0

def calculate_dp(mn, monomer_mass):
    return mn / monomer_mass if monomer_mass else 0
