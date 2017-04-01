from parser import Parser
from composer import Composer

p = Parser()
a = p.get_args()
composer = Composer(
    length=a.length,
    instruments_list=a.instruments,
    tempo=a.tempo,
    output=a.output,
    samples=a.samples,
    bass_sample=a.bass,
    sample_length=a.sample_length,
    step=a.step,  # average difference of pitch note change
    tracks=a.tracks,
    intense=a.intense,  # intense of sample in time
    flow_ratio=a.flow_ratio,  # frequency of note pitch change ratio <-(0,100)
    seed_ratio=a.seed_ratio,  # frequency of seeding in harmonical samples<-(0,100)
    seed_range=a.seed_range,  # range of seeding in harmonical samples <-(0,100)
    down_willing_ratio=a.down_ratio,  # ratio of getting low witch pitch in harmonical samples
    jump=a.jump,  # avarega pitch diference in bass line
    rude=a.rude,  # ratio of ignoring parameters, and gerating random in bassline
    key=a.key,  # key in which music is generated
    losing=a.losing
)
composer.compose()
