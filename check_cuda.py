import torch
#torch.backends.cudnn.benchmark 被設置為 False。這意味著在使用CUDA時，不會自動對CuDNN進行性能基準測試。通常，CuDNN基準測試在不同設備上可能會產生不同的結果，因此將其設置為 False 可以確保一致的結果，儘管性能可能稍微降低。
#torch.backends.cudnn.deterministic 被設置為 True。這個選項確保使用CUDA時計算結果的一致性，即使在不同設備上也是如此。這可能會降低一些性能，但確保了可重現性。
def check_cuda():
    if torch.cuda.is_available():
        torch.backends.cudnn.benchmark = False
        torch.backends.cudnn.deterministic = True
