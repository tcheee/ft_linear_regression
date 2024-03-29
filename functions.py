################################################################################################################################################################################
def estimatePrice(mileage, t0, t1):
    result = float(t0 + (mileage * t1))
    return (result)
###############################################################################################################################################################################
def get_estimatePrice(miles, t0, t1, P_raw):
    result = unnormalise_value(estimatePrice(miles, t0, t1), P_raw)
    return (result)
###############################################################################################################################################################################
def normalize_data(dataset):
    result = (dataset - dataset.mean()) / (dataset.max() - dataset.min())
    return (result)
###############################################################################################################################################################################
def unnormalise_data(dataset):
    result = dataset.mean() + dataset * (dataset.max() - dataset.min()) 
    return (result)
###############################################################################################################################################################################
def normalize_value(value, dataset):
    result = float((value - dataset.mean()) / (dataset.max() - dataset.min()))
    return (result)
###############################################################################################################################################################################
def unnormalise_value(value, dataset):
    result = float(dataset.mean() + value * (dataset.max() - dataset.min()))
    return (result)
###############################################################################################################################################################################
def get_r2_precision(P_raw, K_raw, t0, t1):
    S0 = 0
    S1 = 0
    mean = P_raw.mean()
    for i in range(len(P_raw)):
        S0 += ((P_raw[i] - get_estimatePrice(normalize_value(K_raw[i], K_raw), t0, t1, P_raw)) ** 2)
        S1 += ((P_raw[i] - mean) ** 2)
    S = S0 / S1
    result = int((1 - S) * 100)
    return (result)
###############################################################################################################################################################################