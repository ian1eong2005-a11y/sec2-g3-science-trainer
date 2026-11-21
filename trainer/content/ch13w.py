"""Ch 13 (G3): calculation templates adapted from Ws 1-3 (2026), the Mastery Tests and Quizzes 13.1-13.4:
power = energy / time, kWh = kW x h, cost = kWh x tariff, series / parallel readings. Numbers vary on every serve."""
from .. import sketches as S
from .base import fmt, md_table, nice, numeric_options, pick, template, text_options

SRC = "_Adapted from the QTSS Ch 13 worksheets and mastery tests._"


def money(x):
    return f"${x:,.2f}"


# ---------------------------------------------------------------- L1
@template("c13w_lamp_power", chapter=13, level=1, lo="13.6")
def lamp_power(rng):
    P = nice(rng, 60, 100, 120)
    t = nice(rng, 5, 6, 10)
    E = P * t
    opts, key, mis = numeric_options(rng, P, [
        (E * t, "Power = energy ÷ time; do not multiply."),
        (t / E, "Upside down: energy ÷ time."),
        (E, "That is the energy; divide by the seconds."),
    ], unit="W", sf=3)
    return dict(
        stem=f"An electric lamp transfers energy.\n\n{md_table(['energy transferred / J', 'time / s'], [[E, t]])}\n\nCalculate the power of the lamp.",
        options=opts, key=key, misconceptions=mis,
        formula="power = energy transferred ÷ time",
        working=[f"P = {E} ÷ {t}", f"= **{P} W**", SRC],
        hints=["Power = energy ÷ time.", f"{E} ÷ {t}.", "Watts."],
    )


@template("c13w_aircon_kwh", chapter=13, level=1, lo="13.7*")
def aircon_kwh(rng):
    Pk = nice(rng, 1.2, 1.5, 2)
    h = nice(rng, 6, 8, 10)
    E = Pk * h
    opts, key, mis = numeric_options(rng, E, [
        (Pk / h, "Energy = power × time; do not divide."),
        (Pk * h * 1000, "The power is already in kW, so the answer is in kWh."),
        (Pk, "Multiply by the hours."),
    ], unit="kWh", sf=3)
    return dict(
        stem=f"An air conditioner is used.\n\n{md_table(['power rating / kW', 'time used / h'], [[Pk, h]])}\n\nCalculate the energy used, in kWh.",
        options=opts, key=key, misconceptions=mis,
        formula="energy (kWh) = power (kW) × time (h)",
        working=[f"E = {Pk:g} × {h}", f"= **{E:g} kWh**", SRC],
        hints=["kW × h gives kWh.", f"{Pk:g} × {h}.", "No unit changes needed."],
    )


@template("c13w_cost_from_kwh_cents", chapter=13, level=1, lo="13.7*")
def cost_from_kwh_cents(rng):
    E = nice(rng, 4.8, 6, 9.6, 12)
    cents = nice(rng, 20, 25, 30)
    c = E * cents
    opts, key, mis = numeric_options(rng, c, [
        (E / cents, "Cost = kWh × price per kWh; do not divide."),
        (E + cents, "Multiply, do not add."),
        (c / 100, "The price is in cents, so the answer is in cents."),
    ], unit="cents", sf=3)
    return dict(
        stem=f"Electricity costs **{cents} cents per kWh**.\n\n{md_table(['energy used / kWh'], [[E]])}\n\nCalculate the cost, in cents.",
        options=opts, key=key, misconceptions=mis,
        formula="cost = energy (kWh) × price per kWh",
        working=[f"cost = {E:g} × {cents}", f"= **{c:g} cents**", SRC],
        hints=["Each kWh costs the tariff.", f"{E:g} × {cents}.", "Cents."],
    )


# ---------------------------------------------------------------- L2
@template("c13w_energy_from_cost", chapter=13, level=2, lo="13.7*")
def energy_from_cost(rng):
    cents = nice(rng, 20, 25, 30)
    E = nice(rng, 1.2, 1.5, 2.4)
    c = E * cents
    opts, key, mis = numeric_options(rng, E, [
        (c * cents, "Energy = cost ÷ tariff; do not multiply."),
        (cents / c, "Upside down: cost ÷ tariff."),
        (c, "That is the cost; divide by the price per kWh."),
    ], unit="kWh", sf=3)
    return dict(
        stem=f"Using a kettle cost **{c:g} cents**. Electricity costs **{cents} cents per kWh**.\n\n{md_table(['cost / cents', 'tariff / cents per kWh'], [[f'{c:g}', cents]])}\n\nCalculate the energy used.",
        options=opts, key=key, misconceptions=mis,
        formula="energy = cost ÷ tariff",
        working=[f"E = {c:g} ÷ {cents}", f"= **{E:g} kWh**", SRC],
        hints=["Rearrange cost = kWh × tariff.", "kWh = cost ÷ tariff.", f"{c:g} ÷ {cents}."],
    )


@template("c13w_time_minutes_from_kwh", chapter=13, level=2, lo="13.7*")
def time_minutes_from_kwh(rng):
    Pk = nice(rng, 1.5, 2, 2.5)
    m = nice(rng, 24, 30, 36, 45)
    E = Pk * m / 60
    opts, key, mis = numeric_options(rng, m, [
        (m / 60, "That is the time in hours; the question asks for minutes."),
        (E / Pk, "Hours × 60 gives minutes."),
        (E * Pk * 60, "time = energy ÷ power."),
    ], unit="min", sf=3)
    return dict(
        stem=f"A kettle is used.\n\n{md_table(['power / kW', 'energy used / kWh'], [[Pk, fmt(E)]])}\n\nFor how many minutes was the kettle used?",
        options=opts, key=key, misconceptions=mis,
        formula="time (h) = energy ÷ power;  minutes = hours × 60",
        working=[f"t = {fmt(E)} ÷ {Pk:g} = {m / 60:g} h", f"= {m / 60:g} × 60 = **{m} min**", SRC],
        hints=["time = energy ÷ power gives hours.", f"{fmt(E)} ÷ {Pk:g}.", "Multiply by 60."],
    )


@template("c13w_kettle_daily_kwh", chapter=13, level=2, lo="13.7*")
def kettle_daily_kwh(rng):
    P = nice(rng, 1500, 2000, 2200)
    m = nice(rng, 12, 15, 20, 30)
    E = P / 1000 * m / 60
    opts, key, mis = numeric_options(rng, E, [
        (P / 1000 * m, "Change the minutes to hours."),
        (P * m / 60, "Change the watts to kilowatts."),
        (P / 1000 / (m / 60), "Multiply power by time; do not divide."),
    ], unit="kWh", sf=3)
    return dict(
        stem=f"A kettle's rating plate reads **{P} W**. It is used for a total of **{m} minutes** a day.\n\n{md_table(['power / W', 'time per day / min'], [[P, m]])}\n\nCalculate the energy it uses in a day, in kWh.",
        options=opts, key=key, misconceptions=mis,
        formula="energy (kWh) = power (kW) × time (h)",
        working=[f"{P} W = {P / 1000:g} kW;  {m} min = {m / 60:g} h", f"E = {P / 1000:g} × {m / 60:g} = **{fmt(E)} kWh**", SRC],
        hints=["Convert W → kW.", f"{m} min = {m / 60:g} h.", "Multiply."],
    )


@template("c13w_parallel_third_ammeter", chapter=13, level=2, lo="13.3*")
def parallel_third_ammeter(rng):
    tot = nice(rng, 0.9, 1.2, 1.5)
    I2 = nice(rng, 0.4, 0.5, 0.6)
    I3 = round(tot - I2, 2)
    opts, key, mis = numeric_options(rng, I3, [
        (tot + I2, "The branch currents ADD UP to the main current: subtract."),
        (tot, "That is the main current; the branch gets only part of it."),
        (I2, "The branches need not be equal; use main − known branch."),
    ], unit="A", sf=2)
    return dict(
        stem=f"Fig. 1 shows two lamps P and Q in parallel. Ammeter A₁ (main) reads **{fmt(tot)} A** and A₂ (in P's branch) reads **{fmt(I2)} A**. What does A₃ (in Q's branch) read?",
        figure=S.circuit(["ammeter"], parallel=[["ammeter", "lamp"], ["ammeter", "lamp"]], top=("cell",), labels=["A₁", "P", "Q"]),
        options=opts, key=key, misconceptions=mis,
        formula="parallel: branch currents add up to the main current",
        working=[f"A₃ = {fmt(tot)} − {fmt(I2)}", f"= **{fmt(I3)} A**", SRC],
        hints=["The main current splits between P and Q.", "Known total, known P: subtract.", f"{fmt(tot)} − {fmt(I2)}."],
    )


# ---------------------------------------------------------------- L3
@template("c13w_tv_kwh_month", chapter=13, level=3, lo="13.7*")
def tv_kwh_month(rng):
    P = nice(rng, 100, 170, 300)
    h = nice(rng, 20, 25, 40)
    E = P / 1000 * h
    opts, key, mis = numeric_options(rng, E, [
        (P * h, "Change the watts to kilowatts."),
        (P / 1000 / h, "Multiply by the hours; do not divide."),
        (P / 1000, "Multiply by the hours."),
    ], unit="kWh", sf=3)
    return dict(
        stem=f"Rosa buys a television and watches it for **{h} hours** in a month.\n\n{md_table(['type', 'power rating / W'], [['plasma TV', P]])}\n\nCalculate the electrical energy used, in kWh.",
        options=opts, key=key, misconceptions=mis,
        formula="energy (kWh) = power (kW) × time (h)",
        working=[f"{P} W = {P / 1000:g} kW", f"E = {P / 1000:g} × {h} = **{fmt(E)} kWh**", SRC],
        hints=["Change W to kW.", f"{P / 1000:g} kW.", f"× {h} h."],
    )


@template("c13w_tariff_from_charge", chapter=13, level=3, lo="13.7*")
def tariff_from_charge(rng):
    E = nice(rng, 6, 7.5, 9, 12)
    rate = nice(rng, 0.25, 0.28, 0.30)
    c = E * rate
    opts, key, mis = numeric_options(rng, rate, [
        (E / c, "Tariff = cost ÷ kWh, not kWh ÷ cost."),
        (c * E, "Divide the cost by the energy."),
        (c, "That is the total charge; divide by the kWh."),
    ], unit="$ per kWh", sf=3, dp=2)
    return dict(
        stem=f"A household is charged for its electricity.\n\n{md_table(['energy used / kWh', 'charge'], [[E, money(c)]])}\n\nCalculate the electricity tariff (price per kWh).",
        options=opts, key=key, misconceptions=mis,
        formula="tariff = cost ÷ energy (kWh)",
        working=[f"tariff = {money(c)} ÷ {E:g}", f"= **{money(rate)} per kWh**", SRC],
        hints=["Rearrange cost = kWh × tariff.", "tariff = cost ÷ kWh.", f"{c:.2f} ÷ {E:g}."],
    )


@template("c13w_most_energy_table", chapter=13, level=3, lo="13.6")
def most_energy_table(rng):
    rows = [["kettle", 2, nice(rng, 0.25, 0.5)], ["aircon", nice(rng, 1, 1.2), nice(rng, 6, 8)], ["fridge", 0.15, 24], ["television", 0.1, nice(rng, 4, 5)], ["fan", 0.05, nice(rng, 8, 10)]]
    Es = [(r[0], r[1] * r[2]) for r in rows]
    best = max(Es, key=lambda x: x[1])
    hp = max(rows, key=lambda r: r[1])
    opts, key, mis = text_options(rng, f"most energy: {best[0]} ({best[1]:g} kWh); highest power: {hp[0]} ({hp[1]:g} kW)", {
        f"most energy: {hp[0]}; highest power: {hp[0]}": "The highest power is not the most energy: energy = power × time.",
        f"most energy: {best[0]}; highest power: {best[0]}": f"The {hp[0]} has the highest power rating.",
        f"most energy: fridge (24 h); highest power: {hp[0]}": f"The fridge runs longest, but 0.15 × 24 = 3.6 kWh is less than {best[1]:g} kWh.",
    })
    return dict(
        stem=f"The table shows five appliances in a flat and how long each is on in a day.\n\n{md_table(['appliance', 'power / kW', 'hours on per day'], rows)}\n\nWhich appliance uses the most energy in a day, and which has the highest power?",
        options=opts, key=key, misconceptions=mis,
        formula="energy = power × time; the most powerful appliance is not always the biggest energy user",
        working=["; ".join(f"{n}: {e:g} kWh" for n, e in Es), f"**most energy {best[0]}, highest power {hp[0]}**", SRC],
        hints=["Multiply power × hours for each appliance.", "Compare the kWh.", "Highest power is just the biggest kW number."],
    )


@template("c13w_series_identical_pd", chapter=13, level=3, lo="13.3*")
def series_identical_pd(rng):
    n = nice(rng, 2, 3, 4)
    V = nice(rng, 6, 9, 12)
    each = V / n
    opts, key, mis = numeric_options(rng, each, [
        (V, "Series lamps SHARE the battery voltage."),
        (V * n, "Divide, do not multiply."),
        (V / (n + 1), f"There are {n} lamps sharing equally."),
    ], unit="V", sf=3)
    return dict(
        stem=f"**{n}** identical lamps are connected in series to a **{V} V** battery.\n\n{md_table(['lamps in series', 'battery voltage / V'], [[n, V]])}\n\nWhat is the potential difference across each lamp?",
        options=opts, key=key, misconceptions=mis,
        formula="series: the voltages across the components add up to the battery voltage; identical lamps share equally",
        working=[f"{V} V shared by {n} identical lamps", f"= {V} ÷ {n} = **{fmt(each)} V**", SRC],
        hints=["In series the voltages add up to the battery's.", "Identical lamps take equal shares.", f"{V} ÷ {n}."],
    )


# ---------------------------------------------------------------- L4
@template("c13w_aircon_month_cost", chapter=13, level=4, lo="13.7*")
def aircon_month_cost(rng):
    E_day = nice(rng, 6, 8, 9.6)
    days = 30
    rate = nice(rng, 0.25, 0.30)
    c = E_day * days * rate
    opts, key, mis = numeric_options(rng, c, [
        (E_day * rate, "That is one day; multiply by 30 days."),
        (E_day * days, "That is the energy in kWh; multiply by the price."),
        (E_day * days * rate * 100, "The price is in dollars already."),
    ], unit="$", sf=4, dp=2)
    return dict(
        stem=f"An aircon uses **{E_day:g} kWh** each night. Electricity costs {money(rate)} per kWh.\n\n{md_table(['energy per night / kWh', 'nights', 'price per kWh'], [[E_day, days, money(rate)]])}\n\nCalculate the cost of running the aircon for {days} nights.",
        options=opts, key=key, misconceptions=mis,
        formula="energy = kWh per night × nights;  cost = kWh × price",
        working=[f"E = {E_day:g} × {days} = {E_day * days:g} kWh", f"cost = {E_day * days:g} × {money(rate)} = **{money(c)}**", SRC],
        hints=["Find the kWh for the month.", f"{E_day:g} × {days}.", f"× {rate}."],
    )


@template("c13w_fan_vs_aircon_saving", chapter=13, level=4, lo="13.7*")
def fan_vs_aircon_saving(rng):
    Pa = nice(rng, 1, 1.2)
    Pf = nice(rng, 0.05, 0.06, 0.075)
    h = nice(rng, 7, 8, 10)
    saving = (Pa - Pf) * h
    opts, key, mis = numeric_options(rng, saving, [
        (Pa * h, "That is the aircon's energy; subtract the fan's energy."),
        (Pf * h, "That is the fan's energy, not the saving."),
        ((Pa - Pf), "Multiply the power difference by the hours."),
    ], unit="kWh", sf=3)
    return dict(
        stem=f"A family replaces its aircon with a fan for the same **{h} hours** a night.\n\n{md_table(['appliance', 'power / kW'], [['aircon', Pa], ['fan', Pf]])}\n\nHow much energy do they save each night?",
        options=opts, key=key, misconceptions=mis,
        formula="saving = (aircon power − fan power) × time",
        working=[f"aircon: {Pa:g} × {h} = {Pa * h:g} kWh;  fan: {Pf:g} × {h} = {Pf * h:g} kWh", f"saving = {Pa * h:g} − {Pf * h:g} = **{fmt(saving)} kWh**", SRC],
        hints=["Work out each appliance's kWh.", "Subtract.", f"({Pa:g} − {Pf:g}) × {h}."],
    )


@template("c13w_lamp_removed_reading", chapter=13, level=4, lo="13.3*")
def lamp_removed_reading(rng):
    I_p = nice(rng, 0.5, 0.6, 0.8)
    I_q = nice(rng, 0.2, 0.3, 0.4)
    tot = round(I_p + I_q, 2)
    opts, key, mis = text_options(rng, f"A₁ reads {fmt(I_p)} A, because only P's branch is left and its current is unchanged", {
        f"A₁ reads {fmt(tot)} A, because the main current does not change": "Q's branch no longer carries current, so the main current falls to P's current.",
        f"A₁ reads 0 A, because removing a lamp breaks the circuit": "In parallel, P still has its own complete path.",
        f"A₁ reads {fmt(tot)} A, because P now takes Q's current as well": "P still has the same voltage across it, so its current is unchanged.",
    })
    return dict(
        stem=f"Fig. 1 shows lamps P and Q in parallel. A₁ (main) reads **{fmt(tot)} A** and A₂ (P's branch) reads **{fmt(I_p)} A**. Lamp Q is then removed from its holder. What does A₁ read now, and why?",
        figure=S.circuit(["ammeter"], parallel=[["ammeter", "lamp"], ["lamp"]], top=("cell",), labels=["A₁", "P", "Q"]),
        options=opts, key=key, misconceptions=mis,
        formula="parallel: each branch has the full cell voltage, so removing one branch leaves the others' currents unchanged; main current = sum of remaining branches",
        working=[f"Q's branch ({fmt(I_q)} A) is gone; P still has the full cell voltage so its current stays {fmt(I_p)} A", f"A₁ = **{fmt(I_p)} A**", SRC],
        hints=["Does P still have a complete path?", "Does P's voltage change?", "Main current = P's current only."],
    )


@template("c13w_lamps_not_identical", chapter=13, level=4, lo="13.3*")
def lamps_not_identical(rng):
    V = nice(rng, 6, 9, 12)
    Vx = round(V * nice(rng, 0.6, 2 / 3, 0.7), 1)
    Vy = round(V - Vx, 1)
    opts, key, mis = text_options(rng, f"Y reads {Vy:g} V; X has the larger resistance because it takes the bigger share of the voltage", {
        f"Y reads {Vx:g} V; the lamps are identical": f"The two voltages must add up to {V} V, so Y has {Vy:g} V.",
        f"Y reads {Vy:g} V; Y has the larger resistance": "The lamp with the larger resistance takes the LARGER share of the voltage: that is X.",
        f"Y reads {V} V; each lamp gets the full battery voltage": "That is true in parallel; in series the voltages are shared.",
    })
    return dict(
        stem=f"Fig. 1 shows two lamps X and Y in series with a **{V} V** battery. A voltmeter across X reads **{Vx:g} V**. What does a voltmeter across Y read, and what does this tell you about the lamps?",
        figure=S.circuit(["lamp", "lamp"], top=("battery",), voltmeter_across=0, labels=["X", "Y"]),
        options=opts, key=key, misconceptions=mis,
        formula="series: voltages add up to the battery voltage; the larger resistance takes the larger share",
        working=[f"Y = {V} − {Vx:g} = {Vy:g} V", f"X takes more than half, so **X has the larger resistance**", SRC],
        hints=["The two voltages add up to the battery voltage.", f"{V} − {Vx:g}.", "Which lamp takes the bigger share?"],
    )


# ---------------------------------------------------------------- L5
@template("c13w_adaptor_overload", chapter=13, level=5, lo="13.5")
def adaptor_overload(rng):
    apps = [("aircon", nice(rng, 1000, 1200)), ("heater", nice(rng, 1500, 2000)), ("kettle", nice(rng, 2000, 2200)), ("hair dryer", nice(rng, 1200, 1500))]
    V = 230
    tot = sum(P for _, P in apps) / V
    limit = 13
    opts, key, mis = text_options(rng, f"about {fmt(tot)} A, more than the {limit} A limit, so the adaptor's wires would overheat and could start a fire", {
        f"about {fmt(tot / 4)} A, within the {limit} A limit, so it is safe": "The currents of all four appliances ADD UP in the adaptor.",
        f"about {fmt(sum(P for _, P in apps) / 1000)} A, within the {limit} A limit": "Current = power ÷ voltage, with the voltage 230 V, not 1000.",
        f"about {fmt(tot)} A, but it is safe because the voltage stays 230 V": "The problem is the large CURRENT heating the wires, not the voltage.",
    })
    return dict(
        stem=f"Four appliances are plugged into one adaptor rated **{limit} A** on the **{V} V** mains.\n\n{md_table(['appliance', 'power / W'], [[n, P] for n, P in apps])}\n\nWhat total current flows through the adaptor, and why is this dangerous?",
        options=opts, key=key, misconceptions=mis,
        formula="current = power ÷ voltage for each appliance; the currents add up in the adaptor",
        working=[f"total power = {sum(P for _, P in apps)} W", f"total current = {sum(P for _, P in apps)} ÷ {V} = {fmt(tot)} A > {limit} A", "the wires overheat (fire risk): **overloading**", SRC],
        hints=["Add the powers, then divide by 230 V.", f"{sum(P for _, P in apps)} ÷ 230.", "Compare with 13 A."],
    )


@template("c13w_fuse_choice_calc", chapter=13, level=5, lo="13.5")
def fuse_choice_calc(rng):
    P = nice(rng, 1800, 2000, 2300)
    V = 230
    I = P / V
    fuses = [3, 5, 13]
    chosen = min(f for f in fuses if f > I)
    opts, key, mis = text_options(rng, f"current about {fmt(I)} A, so the {chosen} A fuse: the smallest rating above the normal current", {
        f"current about {fmt(I)} A, so the 5 A fuse: closest to the current": f"5 A is BELOW {fmt(I)} A, so it would melt in normal use.",
        f"current about {fmt(I)} A, so the 3 A fuse: the safest because it is smallest": "A fuse below the normal current blows at once.",
        f"current about {fmt(P / 1000)} A, so the 3 A fuse": "Current = power ÷ 230 V, not power ÷ 1000.",
    })
    return dict(
        stem=f"A kettle is rated **{P} W, {V} V**. Fuses of **3 A, 5 A and 13 A** are available.\n\n{md_table(['power / W', 'voltage / V'], [[P, V]])}\n\nWhat current does the kettle draw, and which fuse should be fitted?",
        options=opts, key=key, misconceptions=mis,
        formula="current = power ÷ voltage; choose the smallest fuse rating above the normal current",
        working=[f"I = {P} ÷ {V} = {fmt(I)} A", f"smallest fuse above {fmt(I)} A: **{chosen} A**", SRC],
        hints=["Find the normal current first.", f"{P} ÷ 230.", "The fuse must not melt in normal use."],
    )


@template("c13w_month_two_appliances", chapter=13, level=5, lo="13.7*")
def month_two_appliances(rng):
    P1, h1 = nice(rng, 1000, 1200), nice(rng, 6, 8)
    P2, h2 = nice(rng, 2000, 2200), nice(rng, 0.25, 0.5)
    rate = nice(rng, 0.25, 0.30)
    days = 30
    E = (P1 / 1000 * h1 + P2 / 1000 * h2) * days
    c = E * rate
    opts, key, mis = numeric_options(rng, c, [
        ((P1 / 1000 * h1 + P2 / 1000 * h2) * rate, "That is one day; multiply by 30 days."),
        (P1 / 1000 * h1 * days * rate, "Add the kettle's energy as well."),
        (E, "That is the energy in kWh; multiply by the price."),
    ], unit="$", sf=4, dp=2)
    return dict(
        stem=f"A flat uses two appliances every day. Electricity costs {money(rate)} per kWh.\n\n{md_table(['appliance', 'power / W', 'hours per day'], [['aircon', P1, h1], ['kettle', P2, h2]])}\n\nCalculate the cost for **{days} days**.",
        options=opts, key=key, misconceptions=mis,
        formula="kWh = kW × h for each; add; × days; cost = kWh × price",
        working=[f"per day: {P1 / 1000:g} × {h1} + {P2 / 1000:g} × {h2:g} = {P1 / 1000 * h1 + P2 / 1000 * h2:g} kWh", f"{days} days: {E:g} kWh", f"cost = {E:g} × {money(rate)} = **{money(c)}**", SRC],
        hints=["Work out each appliance's kWh per day.", "Add, then × 30.", f"× {rate}."],
    )
