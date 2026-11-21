"""Ch 9 (G3): calculation templates adapted from the CH 9 revision worksheet (2026), the Mastery Tests and Quizzes 9.1-9.4:
weight = mg, pressure = force / area, KE = 1/2 m v^2, GPE = mgh and energy conservation. Numbers vary on every serve."""
import math

from .. import figs, sketches as S
from .base import fmt, md_table, nice, numeric_options, pick, template, text_options

SRC = "_Adapted from the QTSS Ch 9 revision worksheet and mastery tests._"
G = 10


# ---------------------------------------------------------------- L1
@template("c09w_weight_from_mass", chapter=9, level=1, lo="9.1*")
def weight_from_mass(rng):
    m = nice(rng, 40, 50, 60, 75)
    W = m * G
    opts, key, mis = numeric_options(rng, W, [
        (m, "That is the mass in kg; weight = mass × g."),
        (m / G, "Multiply by g, do not divide."),
        (m * 9, "Use g = 10 N/kg, as in the question."),
    ], unit="N", sf=3)
    return dict(
        stem=f"A skier stands on snow. Take g = 10 N/kg.\n\n{md_table(['mass of skier / kg'], [[m]])}\n\nCalculate the weight of the skier.",
        options=opts, key=key, misconceptions=mis,
        formula="weight = mass × g",
        working=[f"W = {m} × 10", f"= **{W} N**", SRC],
        hints=["Weight is a force: mass × gravitational field strength.", "g = 10 N/kg.", f"{m} × 10."],
    )


@template("c09w_pressure_simple", chapter=9, level=1, lo="9.2*")
def pressure_simple(rng):
    F = nice(rng, 20, 30, 40, 60)
    A = nice(rng, 0.002, 0.004, 0.005, 0.01)
    P = F / A
    opts, key, mis = numeric_options(rng, P, [
        (F * A, "Pressure = force ÷ area; do not multiply."),
        (A / F, "Upside down: force ÷ area."),
        (F, "That is the force; divide by the area."),
    ], unit="N/m²", sf=3)
    return dict(
        stem=f"A block rests on a table.\n\n{md_table(['force on the table / N', 'area of contact / m²'], [[F, A]])}\n\nCalculate the pressure on the table.",
        options=opts, key=key, misconceptions=mis,
        formula="pressure = force ÷ area",
        working=[f"P = {F} ÷ {A}", f"= **{fmt(P)} N/m²**", SRC],
        hints=["Pressure = force ÷ area.", f"{F} ÷ {A}.", "The unit N/m² is also called the pascal."],
    )


@template("c09w_ke_car", chapter=9, level=1, lo="9.4*")
def ke_car(rng):
    m = nice(rng, 800, 1000, 1200)
    v = nice(rng, 5, 8, 10)
    KE = 0.5 * m * v ** 2
    opts, key, mis = numeric_options(rng, KE, [
        (m * v ** 2, "You forgot the half."),
        (0.5 * m * v, "The speed must be squared."),
        (m * v, "KE = ½ × m × v²."),
    ], unit="J", sf=3)
    return dict(
        stem=f"A car moves along a road.\n\n{md_table(['mass / kg', 'speed / m/s'], [[m, v]])}\n\nCalculate the energy in the car's kinetic store.",
        options=opts, key=key, misconceptions=mis,
        formula="KE = ½ × mass × speed²",
        working=[f"KE = ½ × {m} × {v}²", f"= **{fmt(KE, sf=4)} J**", SRC],
        hints=["Square the speed first.", f"{v}² = {v ** 2}.", f"½ × {m} × {v ** 2}."],
    )


@template("c09w_gpe_slab", chapter=9, level=1, lo="9.4*")
def gpe_slab(rng):
    m = nice(rng, 2, 3, 5, 8)
    h = nice(rng, 1.2, 1.5, 2)
    E = m * G * h
    opts, key, mis = numeric_options(rng, E, [
        (m * h, "You forgot g = 10 N/kg."),
        (m * G, "Multiply by the height as well."),
        (m * G / h, "GPE = m × g × h: multiply, do not divide."),
    ], unit="J", sf=3)
    return dict(
        stem=f"A builder lifts a concrete slab onto a lorry. Take g = 10 N/kg.\n\n{md_table(['mass of slab / kg', 'height lifted / m'], [[m, h]])}\n\nCalculate the energy gained in the slab's gravitational potential store.",
        options=opts, key=key, misconceptions=mis,
        formula="GPE = mass × g × height",
        working=[f"GPE = {m} × 10 × {h:g}", f"= **{fmt(E)} J**", SRC],
        hints=["GPE = m × g × h.", "g = 10 N/kg.", f"{m} × 10 × {h:g}."],
    )


# ---------------------------------------------------------------- L2
@template("c09w_weight_from_pressure", chapter=9, level=2, lo="9.2*")
def weight_from_pressure(rng):
    a, b = nice(rng, 0.4, 0.5), nice(rng, 0.6, 0.8)
    P = nice(rng, 200, 250, 300)
    W = P * a * b
    opts, key, mis = numeric_options(rng, W, [
        (P / (a * b), "Weight = pressure × area; do not divide."),
        (P * a, "The area is length × width."),
        (P, "That is the pressure; multiply by the area."),
    ], unit="N", sf=3)
    return dict(
        stem=f"Fig. 1 shows a brick standing on the ground on its {a:g} m by {b:g} m face. It exerts a pressure of **{P} N/m²**. Calculate the weight of the brick.",
        figure=S.block_area(a, b, f"{P} N/m²", unit="m"),
        options=opts, key=key, misconceptions=mis,
        formula="weight (force) = pressure × area",
        working=[f"area = {a:g} × {b:g} = {a * b:g} m²", f"W = {P} × {a * b:g} = **{fmt(W)} N**", SRC],
        hints=["Find the area of the face on the ground.", f"{a:g} × {b:g}.", "Rearrange pressure = force ÷ area."],
    )


@template("c09w_area_per_leg", chapter=9, level=2, lo="9.2*")
def area_per_leg(rng):
    W = nice(rng, 40, 60, 80)
    P = nice(rng, 5000, 10000, 20000)
    A = W / P
    per = A / 4
    opts, key, mis = numeric_options(rng, per, [
        (A, "That is the TOTAL area of all four legs."),
        (P / W, "Upside down: area = force ÷ pressure."),
        (A * 4, "Divide the total area by 4 legs; do not multiply."),
    ], unit="m²", sf=3)
    return dict(
        stem=f"A small table stands on four legs.\n\n{md_table(['weight of table / N', 'pressure on the floor / Pa'], [[W, P]])}\n\nCalculate the area of contact of EACH leg.",
        options=opts, key=key, misconceptions=mis,
        formula="total area = force ÷ pressure;  area per leg = total ÷ 4",
        working=[f"total area = {W} ÷ {P} = {fmt(A)} m²", f"each leg = {fmt(A)} ÷ 4 = **{fmt(per)} m²**", SRC],
        hints=["Rearrange pressure = force ÷ area.", f"total area = {W} ÷ {P}.", "Then share between 4 legs."],
    )


@template("c09w_mass_from_gpe", chapter=9, level=2, lo="9.4*")
def mass_from_gpe(rng):
    h = nice(rng, 12, 15, 20)
    m = nice(rng, 500, 800, 1000)
    E = m * G * h
    opts, key, mis = numeric_options(rng, m, [
        (E / h, "Divide by g × h, not just h."),
        (E / G, "Divide by g × h, not just g."),
        (E * G * h, "Rearrange: m = GPE ÷ (g × h)."),
    ], unit="kg", sf=3)
    return dict(
        stem=f"A pump raises water from a well that is **{h} m** deep. Take g = 10 N/kg.\n\n{md_table(['energy gained in the gravitational potential store / J'], [[E]])}\n\nCalculate the mass of water raised.",
        options=opts, key=key, misconceptions=mis,
        formula="GPE = m g h  →  m = GPE ÷ (g × h)",
        working=[f"{E} = m × 10 × {h}", f"m = {E} ÷ {G * h} = **{m} kg**", SRC],
        hints=["Write GPE = m × g × h with the numbers in.", f"g × h = {G * h}.", f"{E} ÷ {G * h}."],
    )


@template("c09w_height_from_gpe", chapter=9, level=2, lo="9.4*")
def height_from_gpe(rng):
    m = nice(rng, 1200, 1600, 3200)
    h = nice(rng, 4, 5, 8)
    E = m * G * h
    opts, key, mis = numeric_options(rng, h, [
        (E / m, "Divide by m × g, not just m."),
        (E / G, "Divide by m × g, not just g."),
        (E / (m * G) / 2, "Check: h = GPE ÷ (m × g)."),
    ], unit="m", sf=3)
    return dict(
        stem=f"A car drives up a slope. Take g = 10 N/kg.\n\n{md_table(['mass of car / kg', 'energy gained in gravitational potential store / J'], [[m, E]])}\n\nCalculate the height of the slope.",
        options=opts, key=key, misconceptions=mis,
        formula="h = GPE ÷ (m × g)",
        working=[f"{E} = {m} × 10 × h", f"h = {E} ÷ {m * G} = **{h} m**", SRC],
        hints=["Write GPE = m × g × h.", f"m × g = {m * G}.", f"{E} ÷ {m * G}."],
    )


# ---------------------------------------------------------------- L3
@template("c09w_speed_from_ke", chapter=9, level=3, lo="9.4*")
def speed_from_ke(rng):
    m = nice(rng, 2, 4, 8)
    v = nice(rng, 0.5, 0.8, 1.2, 2)
    KE = 0.5 * m * v ** 2
    opts, key, mis = numeric_options(rng, v, [
        (v ** 2, "You found v²; take the square root."),
        (KE / m, "KE = ½ m v²: divide by ½ m, then square-root."),
        (math.sqrt(KE / m), "Divide by ½ × m (that is, by {0}), not by m.".format(0.5 * m)),
    ], unit="m/s", sf=3)
    return dict(
        stem=f"Jason pushes a trolley.\n\n{md_table(['mass of trolley / kg', 'energy in kinetic store / J'], [[m, fmt(KE)]])}\n\nCalculate the speed of the trolley.",
        options=opts, key=key, misconceptions=mis,
        formula="KE = ½ m v²  →  v² = KE ÷ (½ m)  →  v = √(v²)",
        working=[f"{fmt(KE)} = ½ × {m} × v²", f"v² = {fmt(KE)} ÷ {0.5 * m:g} = {v ** 2:g}", f"v = √{v ** 2:g} = **{fmt(v)} m/s**", SRC],
        hints=["Rearrange for v².", f"½ × m = {0.5 * m:g}.", "Take the square root at the end."],
    )


@template("c09w_ski_area", chapter=9, level=3, lo="9.2*")
def ski_area(rng):
    m = nice(rng, 50, 60, 80)
    P = nice(rng, 400, 500, 800)
    W = m * G
    A = W / P
    opts, key, mis = numeric_options(rng, A, [
        (m / P, "Use the WEIGHT (mass × 10), not the mass."),
        (P / W, "Upside down: area = force ÷ pressure."),
        (W * P, "Divide, do not multiply."),
    ], unit="m²", sf=3)
    return dict(
        stem=f"A skier stands on snow. Take g = 10 N/kg.\n\n{md_table(['mass of skier / kg', 'pressure on the snow / Pa'], [[m, P]])}\n\nCalculate the total base area of the skis.",
        options=opts, key=key, misconceptions=mis,
        formula="weight = m g;  area = weight ÷ pressure",
        working=[f"W = {m} × 10 = {W} N", f"A = {W} ÷ {P} = **{fmt(A)} m²**", SRC],
        hints=["First find the weight.", f"{W} N.", f"Then {W} ÷ {P}."],
    )


@template("c09w_shoes_pressure", chapter=9, level=3, lo="9.2*")
def shoes_pressure(rng):
    W = nice(rng, 600, 720, 840)
    heel = nice(rng, 0.004, 0.005)
    sole = nice(rng, 0.016, 0.02)
    A = 2 * (heel + sole)
    P = W / A
    opts, key, mis = numeric_options(rng, P, [
        (W / (heel + sole), "There are TWO shoes: double the area."),
        (W / sole, "Add the heel and sole areas of both shoes."),
        (W * A, "Pressure = force ÷ area."),
    ], unit="N/m²", sf=3)
    return dict(
        stem=f"A person weighing **{W} N** stands in a pair of shoes. The table shows the area of each part of ONE shoe touching the ground.\n\n{md_table(['part', 'area / m²'], [['heel', heel], ['sole', sole]])}\n\nCalculate the pressure under the shoes.",
        options=opts, key=key, misconceptions=mis,
        formula="total area = 2 × (heel + sole);  pressure = weight ÷ total area",
        working=[f"total area = 2 × ({heel} + {sole}) = {A:g} m²", f"P = {W} ÷ {A:g} = **{fmt(P)} N/m²**", SRC],
        hints=["Add the heel and sole of one shoe.", "Double it for two shoes.", f"{W} ÷ {A:g}."],
    )


@template("c09w_glass_breaks", chapter=9, level=3, lo="9.2*")
def glass_breaks(rng):
    limit = nice(rng, 12000, 15000, 16500)
    F = nice(rng, 25, 35, 50)
    A = nice(rng, 0.0025, 0.004, 0.002)
    P = F / A
    breaks = P > limit
    ans = f"{fmt(P)} N/cm², so the glass {'breaks' if breaks else 'does not break'}"
    opts, key, mis = text_options(rng, ans, {
        f"{fmt(P)} N/cm², so the glass {'does not break' if breaks else 'breaks'}": f"Compare {fmt(P)} with the limit of {limit}.",
        f"{fmt(F * A)} N/cm², so the glass does not break": "Pressure = force ÷ area; do not multiply.",
        f"{F} N/cm², so the glass does not break": "The force must be divided by the area to get the pressure.",
    })
    return dict(
        stem=f"Tempered glass on a phone can withstand a pressure of **{limit} N/cm²**. A sharp object hits it.\n\n{md_table(['force / N', 'area of the point / cm²'], [[F, A]])}\n\nWhat pressure does the object exert, and does the glass break?",
        options=opts, key=key, misconceptions=mis,
        formula="pressure = force ÷ area; compare with the limit",
        working=[f"P = {F} ÷ {A} = {fmt(P)} N/cm²", f"{fmt(P)} {'>' if breaks else '<'} {limit}: **{ans}**", SRC],
        hints=["Work out force ÷ area.", f"{F} ÷ {A}.", "Compare with the limit."],
    )


# ---------------------------------------------------------------- L4
@template("c09w_slope_gpe_to_speed", chapter=9, level=4, lo="9.4*")
def slope_gpe_to_speed(rng):
    m = nice(rng, 40, 50, 60)
    h = nice(rng, 1.8, 2, 3.2)
    E = m * G * h
    v = math.sqrt(2 * G * h)
    opts, key, mis = numeric_options(rng, v, [
        (E / m, "KE = ½ m v²: divide by ½ m, then square-root."),
        (2 * G * h, "That is v²; take the square root."),
        (math.sqrt(G * h), "v² = 2 × KE ÷ m, not KE ÷ m."),
    ], unit="m/s", sf=3)
    return dict(
        stem=f"Dennis carries his skateboard up stairs to point A, **{h:g} m** above point B, then skates down a frictionless slope to B. Take g = 10 N/kg.\n\n{md_table(['mass of Dennis and board / kg'], [[m]])}\n\nCalculate his speed at B.",
        options=opts, key=key, misconceptions=mis,
        formula="GPE at A = KE at B;  m g h = ½ m v²",
        working=[f"GPE = {m} × 10 × {h:g} = {fmt(E)} J = KE at B", f"{fmt(E)} = ½ × {m} × v²  →  v² = {2 * G * h:g}", f"v = √{2 * G * h:g} = **{fmt(v)} m/s**", SRC],
        hints=["Find the GPE at A first.", "All of it becomes KE at B (no friction).", "Then solve ½ m v² = KE."],
    )


@template("c09w_pendulum_height", chapter=9, level=4, lo="9.4*")
def pendulum_height(rng):
    m = nice(rng, 1, 2, 4)
    v = nice(rng, 4, 6, 10)
    KE = 0.5 * m * v ** 2
    h = KE / (m * G)
    opts, key, mis = numeric_options(rng, h, [
        (KE, "That is the kinetic energy in joules, not the height."),
        (KE / m, "Divide by m × g, not just m."),
        (v, "The speed is not the height; use energy conservation."),
    ], unit="m", sf=3)
    return dict(
        stem=f"A pendulum of mass **{m} kg** is released from rest at point A. At the lowest point B its speed is **{v} m/s**. Take g = 10 N/kg and ignore air resistance.\n\n{md_table(['mass / kg', 'speed at B / m/s'], [[m, v]])}\n\nCalculate the height of A above B.",
        options=opts, key=key, misconceptions=mis,
        formula="KE at B = ½ m v² = GPE at A = m g h  →  h = KE ÷ (m g)",
        working=[f"KE at B = ½ × {m} × {v}² = {fmt(KE)} J", f"GPE at A = {fmt(KE)} J = {m} × 10 × h", f"h = {fmt(KE)} ÷ {m * G} = **{fmt(h)} m**", SRC],
        hints=["Find the KE at B.", "By conservation, the GPE at A equals it.", f"h = KE ÷ (m × g)."],
    )


@template("c09w_hydro_speed", chapter=9, level=4, lo="9.4*")
def hydro_speed(rng):
    m = nice(rng, 200, 500, 1000)
    h = nice(rng, 80, 120, 300)
    E = m * G * h
    v = math.sqrt(2 * G * h)
    opts, key, mis = text_options(rng, f"h = {h} m, speed = {fmt(v)} m/s", {
        f"h = {h} m, speed = {fmt(2 * G * h)} m/s": "You found v²; take the square root.",
        f"h = {h * G} m, speed = {fmt(v)} m/s": "h = GPE ÷ (m × g), not GPE ÷ m.",
        f"h = {h} m, speed = {fmt(math.sqrt(G * h))} m/s": "v² = 2 × KE ÷ m: do not forget the 2.",
    })
    return dict(
        stem=f"Water falls from a lake through a pipe to a turbine. Take g = 10 N/kg.\n\n{md_table(['mass of water / kg', 'GPE at the top / J'], [[m, E]])}\n\nFind the height h the water falls, and its speed when it reaches the turbine.",
        options=opts, key=key, misconceptions=mis,
        formula="h = GPE ÷ (m g);  GPE = KE at the bottom = ½ m v²",
        working=[f"h = {E} ÷ ({m} × 10) = {h} m", f"{E} = ½ × {m} × v²  →  v² = {2 * G * h}", f"v = √{2 * G * h} = **{fmt(v)} m/s**", SRC],
        hints=["Height from GPE = m g h.", "All the GPE becomes KE at the bottom.", "Solve ½ m v² = GPE, then square-root."],
    )


@template("c09w_planet_g_table", chapter=9, level=4, lo="9.1*")
def planet_g_table(rng):
    gs = {"A": nice(rng, 4, 5), "B": nice(rng, 9, 10), "C": nice(rng, 6, 7), "D": nice(rng, 8, 8.5)}
    masses = {"A": 3.0, "B": 4.0, "C": 5.0, "D": 6.0}
    rows = [[k, masses[k], round(masses[k] * gs[k], 1)] for k in "ABCD"]
    best = max(gs, key=gs.get)
    opts, key, mis = text_options(rng, best, {k: f"{k}: g = {rows['ABCD'.index(k)][2]} ÷ {masses[k]} = {gs[k]} N/kg, less than {gs[best]} N/kg." for k in "ABCD" if k != best})
    return dict(
        stem=f"The weights of different masses on four planets are shown.\n\n{md_table(['planet', 'mass / kg', 'weight / N'], rows)}\n\nWhich planet has the greatest gravitational field strength?",
        options=opts, key=key, misconceptions=mis,
        formula="g = weight ÷ mass",
        working=["; ".join(f"{k}: {rows['ABCD'.index(k)][2]} ÷ {masses[k]} = {gs[k]} N/kg" for k in "ABCD"), f"greatest: **{best}**", SRC],
        hints=["g = weight ÷ mass for each planet.", "Do not just pick the largest weight.", "Compare the four values of g."],
    )


# ---------------------------------------------------------------- L5
@template("c09w_bullet_mass_then_speed", chapter=9, level=5, lo="9.4*")
def bullet_mass_then_speed(rng):
    v = nice(rng, 300, 400, 500)
    m = nice(rng, 0.01, 0.016, 0.02)
    KE = 0.5 * m * v ** 2
    h = nice(rng, 300, 500, 800)
    E2 = KE + m * G * h
    v2 = math.sqrt(2 * E2 / m)
    opts, key, mis = text_options(rng, f"mass {m:g} kg; speed just before hitting the ground {fmt(v2)} m/s", {
        f"mass {m:g} kg; speed just before hitting the ground {v} m/s": "The bullet also loses GPE as it falls, so its KE and speed increase slightly.",
        f"mass {2 * m:g} kg; speed just before hitting the ground {fmt(v2)} m/s": "m = 2 × KE ÷ v², not KE ÷ v² × 4.",
        f"mass {m:g} kg; speed just before hitting the ground {fmt(math.sqrt(2 * G * h))} m/s": "Add the GPE lost to the KE it already had.",
    })
    return dict(
        stem=f"A bullet flies towards the ground at **{v} m/s** from a height of **{h} m**. Take g = 10 N/kg and ignore air resistance.\n\n{md_table(['energy in the kinetic store / J'], [[fmt(KE)]])}\n\nFind the mass of the bullet and its speed just before it hits the ground.",
        options=opts, key=key, misconceptions=mis,
        formula="m = 2 KE ÷ v²;  total energy at the ground = KE + m g h = ½ m v₂²",
        working=[f"m = 2 × {fmt(KE)} ÷ {v}² = {m:g} kg", f"energy at the ground = {fmt(KE)} + {m:g} × 10 × {h} = {fmt(E2)} J", f"v₂ = √(2 × {fmt(E2)} ÷ {m:g}) = **{fmt(v2)} m/s**", SRC],
        hints=["Rearrange KE = ½ m v² for m.", "Add the GPE lost during the fall.", "Solve for the new speed."],
    )


@template("c09w_balloons_pressure", chapter=9, level=5, lo="9.2*")
def balloons_pressure(rng):
    W = nice(rng, 400, 450, 500)
    area = nice(rng, 0.01, 0.015)
    n = nice(rng, 10, 12, 16)
    pop = nice(rng, 8000, 10000)
    P1 = W / area
    Pn = W / (n * area)
    opts, key, mis = text_options(rng, f"one balloon: {fmt(P1)} Pa (pops); {n} balloons: {fmt(Pn)} Pa (none pops)", {
        f"one balloon: {fmt(P1)} Pa (pops); {n} balloons: {fmt(P1)} Pa (all pop)": "With more balloons the weight is spread over a larger total area, so the pressure on each is lower.",
        f"one balloon: {fmt(W * area)} Pa; {n} balloons: {fmt(W * area * n)} Pa": "Pressure = force ÷ area.",
        f"one balloon: {fmt(P1)} Pa (pops); {n} balloons: {fmt(Pn * n)} Pa (none pops)": f"Divide the weight by the TOTAL area, {n} × {area}.",
    })
    return dict(
        stem=f"A student of weight **{W} N** first presses all her weight onto ONE balloon, then lies on a board resting on **{n}** balloons. Each balloon touches the board over **{area} m²** and pops above **{pop} Pa**.\n\n{md_table(['weight / N', 'area per balloon / m²', 'balloons under the board'], [[W, area, n]])}\n\nWhat is the pressure in each case?",
        options=opts, key=key, misconceptions=mis,
        formula="pressure = force ÷ total area",
        working=[f"one balloon: {W} ÷ {area} = {fmt(P1)} Pa", f"{n} balloons: {W} ÷ ({n} × {area}) = {fmt(Pn)} Pa", SRC],
        hints=["Same weight, different total area.", f"Total area with {n} balloons = {n} × {area}.", "Larger area → smaller pressure."],
    )


@template("c09w_cart_wheels_pressure", chapter=9, level=5, lo="9.2*")
def cart_wheels_pressure(rng):
    W = nice(rng, 2000, 2400, 3000)
    narrow = nice(rng, 0.01, 0.02)
    wide = narrow * nice(rng, 4, 5)
    Pn = W / (4 * narrow)
    Pw = W / (4 * wide)
    opts, key, mis = text_options(rng, f"wide wheels: {fmt(Pw)} Pa against {fmt(Pn)} Pa, so the wide-wheeled cart sinks less", {
        f"narrow wheels: {fmt(Pn)} Pa against {fmt(Pw)} Pa, so the narrow-wheeled cart sinks less": "A HIGHER pressure sinks MORE into soft ground.",
        f"wide wheels: {fmt(W / wide)} Pa against {fmt(W / narrow)} Pa, so the wide-wheeled cart sinks less": "Each cart has four wheels: use 4 × the wheel area.",
        "both sink the same, because the weights are equal": "The same weight on a larger area gives a smaller pressure."},
    )
    return dict(
        stem=f"Two carts of the same weight have four wheels each.\n\n{md_table(['cart', 'contact area of ONE wheel / m²'], [['narrow wheels', narrow], ['wide wheels', wide]])}\n\nThe weight of each cart is **{W} N**. Which cart sinks less into soft ground, and why?",
        options=opts, key=key, misconceptions=mis,
        formula="pressure = weight ÷ (4 × wheel area); lower pressure sinks less",
        working=[f"narrow: {W} ÷ (4 × {narrow}) = {fmt(Pn)} Pa", f"wide: {W} ÷ (4 × {wide:g}) = {fmt(Pw)} Pa", "lower pressure → sinks less: **wide wheels**", SRC],
        hints=["Work out the pressure for each cart.", "Remember four wheels.", "Lower pressure sinks less."],
    )
