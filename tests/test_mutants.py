from simulation.mutants import ep_pcr


def test_ep_pcr():
    wt = "CTAGCTAGGCTCAGTCG"
    mutants = list(ep_pcr(wt, num=10, rate=0.5))
    assert len(mutants) == 10
    for mutant in mutants:
        assert len(mutant) == len(wt)
        for base in mutant:
            assert base in "ACGT"
