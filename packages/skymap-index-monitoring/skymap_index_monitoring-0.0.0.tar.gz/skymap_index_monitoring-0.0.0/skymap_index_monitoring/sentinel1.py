EXPRESSION = {
    'NDVI': '(b8-b6)/(b8+b6)',
    'SAVI': '1.5*(b8-b6)/(b8+b6+0.5)',
    'RECI': 'where(b6 != 0, b8/b6-1, 0);',
    'GCI': 'where(b4 != 0, b8/b4-1, 0);',
    'EVI2': '2.5*(b8-b6)/(b8+2.4*b6+1)',
    'SIPI': 'where((b8-b6) != 0, (b8-b2)/(b8-b6), 0);',
    'NDRE': '(b8-b7)/(b8+b7)',
}