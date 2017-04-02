from main.src.composer import Composer

comp=Composer(200,tempo=250, bass_sample=None, sample_length=10,samples=3,tracks=1, key="c", seed_range=5,seed_ratio=30,flow_ratio=100, intense=100)
comp.compose()



