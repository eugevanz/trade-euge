from talib import CDL2CROWS, CDL3BLACKCROWS, CDL3INSIDE, CDL3LINESTRIKE, CDL3OUTSIDE, CDL3STARSINSOUTH, \
    CDL3WHITESOLDIERS, CDLABANDONEDBABY, CDLADVANCEBLOCK, CDLBELTHOLD, CDLBREAKAWAY, CDLCLOSINGMARUBOZU, \
    CDLCONCEALBABYSWALL, CDLCOUNTERATTACK, CDLDARKCLOUDCOVER, CDLDOJI, CDLDOJISTAR, CDLDRAGONFLYDOJI, CDLENGULFING, \
    CDLEVENINGDOJISTAR, CDLEVENINGSTAR, CDLGAPSIDESIDEWHITE, CDLGRAVESTONEDOJI, CDLHAMMER, CDLHANGINGMAN, CDLHARAMI, \
    CDLHARAMICROSS, CDLHIGHWAVE, CDLHIKKAKE, CDLHIKKAKEMOD, CDLHOMINGPIGEON, CDLIDENTICAL3CROWS, CDLINNECK, \
    CDLINVERTEDHAMMER, CDLKICKING, CDLKICKINGBYLENGTH, CDLLADDERBOTTOM, CDLLONGLEGGEDDOJI, CDLLONGLINE, CDLMARUBOZU, \
    CDLMATCHINGLOW, CDLMATHOLD, CDLMORNINGDOJISTAR, CDLMORNINGSTAR, CDLONNECK, CDLPIERCING, CDLRICKSHAWMAN, \
    CDLRISEFALL3METHODS, CDLSEPARATINGLINES, CDLSHOOTINGSTAR, CDLSHORTLINE, CDLSPINNINGTOP, CDLSTALLEDPATTERN, \
    CDLSTICKSANDWICH, CDLTAKURI, CDLTASUKIGAP, CDLTHRUSTING, CDLTRISTAR, CDLUNIQUE3RIVER, CDLUPSIDEGAP2CROWS, \
    CDLXSIDEGAP3METHODS

# Pattern Recognition Functions
### CDL2CROWS - Two Crows
def two_crows(open_, high, low, close):
    return CDL2CROWS(open_, high, low, close)
### CDL3BLACKCROWS - Three Black Crows
def black_crows(open_, high, low, close):
    return CDL3BLACKCROWS(open_, high, low, close)
### CDL3INSIDE - Three Inside Up/Down
def three_inside(open_, high, low, close):
    return CDL3INSIDE(open_, high, low, close)
### CDL3LINESTRIKE - Three-Line Strike
def three_line_strike(open_, high, low, close):
    return CDL3LINESTRIKE(open_, high, low, close)
### CDL3OUTSIDE - Three Outside Up/Down
def three_outside(open_, high, low, close):
    return CDL3OUTSIDE(open_, high, low, close)
### CDL3STARSINSOUTH - Three Stars In The South
def three_star_in_south(open_, high, low, close):
    return CDL3STARSINSOUTH(open_, high, low, close)
### CDL3WHITESOLDIERS - Three Advancing White Soldiers
def three_white_soldiers(open_, high, low, close):
    return CDL3WHITESOLDIERS(open_, high, low, close)
### CDLABANDONEDBABY - Abandoned Baby
def abandoned_baby(open_, high, low, close):
    return CDLABANDONEDBABY(open_, high, low, close, penetration=0)
### CDLADVANCEBLOCK - Advance Block
def advance_block(open_, high, low, close):
    return CDLADVANCEBLOCK(open_, high, low, close)
### CDLBELTHOLD - Belt-hold
def belt_hold(open_, high, low, close):
    return CDLBELTHOLD(open_, high, low, close)
### CDLBREAKAWAY - Breakaway
def break_away(open_, high, low, close):
    return CDLBREAKAWAY(open_, high, low, close)
### CDLCLOSINGMARUBOZU - Closing Marubozu
def closing_marubozu(open_, high, low, close):
    return CDLCLOSINGMARUBOZU(open_, high, low, close)
### CDLCONCEALBABYSWALL - Concealing Baby Swallow
def conceal_babys_wall(open_, high, low, close):
    return CDLCONCEALBABYSWALL(open_, high, low, close)
### CDLCOUNTERATTACK - Counterattack
def counter_attack(open_, high, low, close):
    return CDLCOUNTERATTACK(open_, high, low, close)
### CDLDARKCLOUDCOVER - Dark Cloud Cover
def dark_cloud_cover(open_, high, low, close):
    return CDLDARKCLOUDCOVER(open_, high, low, close, penetration=0)
### CDLDOJI - Doji
def doji(open_, high, low, close):
    return CDLDOJI(open_, high, low, close)
### CDLDOJISTAR - Doji Star
def doji_star(open_, high, low, close):
    return CDLDOJISTAR(open_, high, low, close)
### CDLDRAGONFLYDOJI - Dragonfly Doji
def dragonfly_doji(open_, high, low, close):
    return CDLDRAGONFLYDOJI(open_, high, low, close)
### CDLENGULFING - Engulfing Pattern
def engulfing(open_, high, low, close):
    return CDLENGULFING(open_, high, low, close)
### CDLEVENINGDOJISTAR - Evening Doji Star
def evening_doji_star(open_, high, low, close):
    return CDLEVENINGDOJISTAR(open_, high, low, close, penetration=0)
### CDLEVENINGSTAR - Evening Star
def evening_star(open_, high, low, close):
    return CDLEVENINGSTAR(open_, high, low, close, penetration=0)
### CDLGAPSIDESIDEWHITE - Up/Down-gap side-by-side white lines
def gap_side_side_white(open_, high, low, close):
    return CDLGAPSIDESIDEWHITE(open_, high, low, close)
### CDLGRAVESTONEDOJI - Gravestone Doji
def gravestone_doji(open_, high, low, close):
    return CDLGRAVESTONEDOJI(open_, high, low, close)
### CDLHAMMER - Hammer
def hammer(open_, high, low, close):
    return CDLHAMMER(open_, high, low, close)
### CDLHANGINGMAN - Hanging Man
def hanging_man(open_, high, low, close):
    return CDLHANGINGMAN(open_, high, low, close)
### CDLHARAMI - Harami Pattern
def harami(open_, high, low, close):
    return CDLHARAMI(open_, high, low, close)
### CDLHARAMICROSS - Harami Cross Pattern
def harami_cross(open_, high, low, close):
    return CDLHARAMICROSS(open_, high, low, close)
### CDLHIGHWAVE - High-Wave Candle
def high_wave(open_, high, low, close):
    return CDLHIGHWAVE(open_, high, low, close)
### CDLHIKKAKE - Hikkake Pattern
def hikkake(open_, high, low, close):
    return CDLHIKKAKE(open_, high, low, close)
### CDLHIKKAKEMOD - Modified Hikkake Pattern
def hikkake_mod(open_, high, low, close):
    return CDLHIKKAKEMOD(open_, high, low, close)
### CDLHOMINGPIGEON - Homing Pigeon
def homing_pigeon(open_, high, low, close):
    return CDLHOMINGPIGEON(open_, high, low, close)
### CDLIDENTICAL3CROWS - Identical Three Crows
def identical_three_crows(open_, high, low, close):
    return CDLIDENTICAL3CROWS(open_, high, low, close)
### CDLINNECK - In-Neck Pattern
def linneck(open_, high, low, close):
    return CDLINNECK(open_, high, low, close)
### CDLINVERTEDHAMMER - Inverted Hammer
def inverted_hammer(open_, high, low, close):
    return CDLINVERTEDHAMMER(open_, high, low, close)
### CDLKICKING - Kicking
def kicking(open_, high, low, close):
    return CDLKICKING(open_, high, low, close)
### CDLKICKINGBYLENGTH - Kicking - bull/bear determined by the longer marubozu
def kicking_by_length(open_, high, low, close):
    return CDLKICKINGBYLENGTH(open_, high, low, close)
### CDLLADDERBOTTOM - Ladder Bottom
def ladder_bottom(open_, high, low, close):
    return CDLLADDERBOTTOM(open_, high, low, close)
### CDLLONGLEGGEDDOJI - Long Legged Doji
def long_legged_doji(open_, high, low, close):
    return CDLLONGLEGGEDDOJI(open_, high, low, close)
### CDLLONGLINE - Long Line Candle
def long_line(open_, high, low, close):
    return CDLLONGLINE(open_, high, low, close)
### CDLMARUBOZU - Marubozu
def marubozu(open_, high, low, close):
    return CDLMARUBOZU(open_, high, low, close)
### CDLMATCHINGLOW - Matching Low
def matching_low(open_, high, low, close):
    return CDLMATCHINGLOW(open_, high, low, close)
### CDLMATHOLD - Mat Hold
def mat_hold(open_, high, low, close):
    return CDLMATHOLD(open_, high, low, close, penetration=0)
### CDLMORNINGDOJISTAR - Morning Doji Star
def morning_doji_star(open_, high, low, close):
    return CDLMORNINGDOJISTAR(open_, high, low, close, penetration=0)
### CDLMORNINGSTAR - Morning Star
def morning_star(open_, high, low, close):
    return CDLMORNINGSTAR(open_, high, low, close, penetration=0)
### CDLONNECK - On-Neck Pattern
def lonneck(open_, high, low, close):
    return CDLONNECK(open_, high, low, close)
### CDLPIERCING - Piercing Pattern
def piercing(open_, high, low, close):
    return CDLPIERCING(open_, high, low, close)
### CDLRICKSHAWMAN - Rickshaw Man
def rickshaw_man(open_, high, low, close):
    return CDLRICKSHAWMAN(open_, high, low, close)
### CDLRISEFALL3METHODS - Rising/Falling Three Methods
def rise_fall_three_methods(open_, high, low, close):
    return CDLRISEFALL3METHODS(open_, high, low, close)
### CDLSEPARATINGLINES - Separating Lines
def separating_lines(open_, high, low, close):
    return CDLSEPARATINGLINES(open_, high, low, close)
### CDLSHOOTINGSTAR - Shooting Star
def shooting_star(open_, high, low, close):
    return CDLSHOOTINGSTAR(open_, high, low, close)
### CDLSHORTLINE - Short Line Candle
def short_line(open_, high, low, close):
    return CDLSHORTLINE(open_, high, low, close)
### CDLSPINNINGTOP - Spinning Top
def spinning_top(open_, high, low, close):
    return CDLSPINNINGTOP(open_, high, low, close)
### CDLSTALLEDPATTERN - Stalled Pattern
def stalled_pattern(open_, high, low, close):
    return CDLSTALLEDPATTERN(open_, high, low, close)
### CDLSTICKSANDWICH - Stick Sandwich
def stick_sandwich(open_, high, low, close):
    return CDLSTICKSANDWICH(open_, high, low, close)
### CDLTAKURI - Takuri (Dragonfly Doji with very long lower shadow)
def takuri(open_, high, low, close):
    return CDLTAKURI(open_, high, low, close)
### CDLTASUKIGAP - Tasuki Gap
def tasuki_gap(open_, high, low, close):
    return CDLTASUKIGAP(open_, high, low, close)
### CDLTHRUSTING - Thrusting Pattern
def thrusting(open_, high, low, close):
    return CDLTHRUSTING(open_, high, low, close)
### CDLTRISTAR - Tristar Pattern
def tri_star(open_, high, low, close):
    return CDLTRISTAR(open_, high, low, close)
### CDLUNIQUE3RIVER - Unique 3 River
def unique_three_river(open_, high, low, close):
    return CDLUNIQUE3RIVER(open_, high, low, close)
### CDLUPSIDEGAP2CROWS - Upside Gap Two Crows
def upside_gap_two_crows(open_, high, low, close):
    return CDLUPSIDEGAP2CROWS(open_, high, low, close)
### CDLXSIDEGAP3METHODS - Upside/Downside Gap Three Methods
def x_side_gap_three_methods(open_, high, low, close):
    return CDLXSIDEGAP3METHODS(open_, high, low, close)
