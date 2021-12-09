def calculateNewFreq(hom_dom, het, hom_rec, mode):
        return abs(float(f"{bool(mode=='p') - (hom_rec + (1/2) * het) / (hom_dom + het + hom_rec):.3f}"))

def grantGeneticPassing(hom_dom, het, hom_rec, live_chance):
        hom_dom = hom_dom * live_chance[0]
        het = het * live_chance[1]
        hom_rec = hom_rec * live_chance[2]
        return hom_dom, het, hom_rec


def calcAllelFreq(dom_freq, rec_freq):
        hom_dom = dom_freq ** 2
        het = 2 * dom_freq * rec_freq
        hom_rec = rec_freq ** 2
        return hom_dom, het, hom_rec

if __name__ == "__main__":
        dom_freq = 0.5
        rec_freq = (1 - dom_freq)
        fitness = [0.25, 1, 0.25]
        hom_dom, het, hom_rec = calcAllelFreq(dom_freq, rec_freq)
        hom_dom, het, hom_rec = grantGeneticPassing(hom_dom, het, hom_rec, fitness)
        newfreq_q = calculateNewFreq(hom_dom, het, hom_rec, "q")
        print(f"Frequences for each allel:\nP: {(1 - newfreq_q):.3f}\nq: {newfreq_q:.3f}")
