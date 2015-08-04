__author__ = 'grahamearley'
import random

from CharacterFrequencyCalibrator import CharacterFrequencyCalibrator


def calculate_score(text, calibrator):
    score = 1
    i = 0
    while i < len(text) - 2:
        code_char_pair = text[i] + text[i + 1]

        if code_char_pair in calibrator.frequencies_dict:
            score *= calibrator.frequencies_dict[code_char_pair]

        i += 1

    return score


def swap_chars_in_text(text, swap_char1, swap_char2):
    # Build up the swapped text:
    swapped_text = ""

    for char in text:
        if char == swap_char1:
            swapped_text += swap_char2
        elif char == swap_char2:
            swapped_text += swap_char1
        else:
            swapped_text += char

    return swapped_text


calibrator = CharacterFrequencyCalibrator("test.txt")

# Jane Austen encrypted sample:
# encrypted_text = "cdsvmce vd ufey, ht vd edde dkifnv it vds. lfy, yvifnv lhknodp mkz qmkd uddy yiodsmlop itydk, hy he kdrds tis umkp vifse yindyvds; mkz, me yvdp moxmpe edd dmbv iyvds hk omsnd uhgdz cmsyhde, hy he hucieehlod yvmy drdsp uiudky evifoz ld ducoipdz hk bikrdsehkn yindyvds. qmkd evifoz yvdsdtisd umjd yvd uiey it drdsp vmot-vifs hk xvhbv evd bmk biuumkz vhe myydkyhik. xvdk evd he edbfsd it vhu, yvdsd xhoo ld uisd odhefsd tis tmoohkn hk oird me ufbv me evd bviiede."

# My own encrypted sample:
encrypted_text = "snon'i j ijmrfn rjojtojrs usju d woyun, dpiunjb ye zjpn jkiunp. d syrn usju mh fnuuno joojptnmnpui sjqn j idmdfjo eongknpxh ji snoi. yp jpyusno pyun, d tknii usn roytojm *byni* wyoc, aku ypfh eyo j xnoujdp usonisyfb ye unlu fnptus? d usdpc usnon'i oyym eyo iymn dpunoniudpt jpjfhidi snon! skvvjs! d jm anekbbfnb usju usdi nlgkdidun ijmrfn bdb pyu ekffh bnxohru wdus usn jxxkojxh d sjb ronikmnb d wykfb inn. mjhsjr d pnnb uy ikrrfh j fjotno qyxjakfjoh iy ji uy roninpu qjodyki jfunopjun joojptnmnpui ye fnuunoi jpb xsjojxunoi, yo wsju sjqn hyk."

encrypted_text = encrypted_text.lower()
letters = "qwertyuiopasdfghjklzxcvbnm"

runtimes = 10000
for run in range(runtimes):
    # print("Initial: " + encrypted_text)

    swap_char1 = random.choice(letters)
    swap_char2 = random.choice(letters)
    # print(" --- Swapping " + swap_char1 + " with " + swap_char2)

    # Determine whether to accept the proposal:
    swapped_text = swap_chars_in_text(encrypted_text, swap_char1, swap_char2)
    proposed_score = calculate_score(swapped_text, calibrator)
    current_score = calculate_score(encrypted_text, calibrator)
    acceptance_ratio = proposed_score / current_score

    unif_rand = random.uniform(0, 1)

    if unif_rand <= acceptance_ratio:  # Accept!
        # print(" ++++ Accepted!")
        encrypted_text = swapped_text
    #     print(encrypted_text)
    # else:
    #     print(" ---- Rejected. ----")

print(encrypted_text)
