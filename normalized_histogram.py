# -*- coding: utf-8 -*-

"""
This algorithm computes the normalized histogram of pixel intensities for a grayscale image
Author: Felipe Andrade
"""

def hist(N, M, P, image):
    counting = {}
    total_pixels = N * M
    for line in image:
        for intensity in line:
            if intensity in counting:
                counting[intensity] += 1
            else:
                counting[intensity] = 1
    histogram = [counting.get(p, 0) / total_pixels for p in range(P)]
    return histogram

while True:
    N, M, P = map(int, input().split())
    if N == -1:
        break

    image = []
    for _ in range(N):
        line = list(map(int, input().split()))
        image.append(line)

    histogram = hist(N, M, P, image)

    for value in histogram:
        print(f'{value:.2f}', end=' ')
    print()
