from wavsound import wavsound

class needlestorage:
    
    """needlestorage object generates needles (subsequence sample) of wavsound
    object data based on number of partitions (num_chunk) and 
    number of samples to be analyzed (limit). The needles/samples are picked
    deterministically so that the data sampled are evenly 
    distributed across the wav file) """
    needles = []
    def __init__(self, wavsound, num_chunks, limit):
        u=0
        x=0
        self.needles = []
        data = wavsound.get_data()
        skips_per_neeedle = max(1,int(len(data)/limit))
        for i in range (len(data)):
            if u >= limit:
                break
            if (x % skips_per_neeedle == 0):
                self.needles.append(data[i:i+int(len(data)/num_chunks)])
                u = u + 1
                # if debug print (i," <--> ",i+int(len(data)/num_chunks))
            x = x + 1
    def pop_unused_needle(self):
        if len(self.needles) == 0:
            return []
        return self.needles.pop(0)
    def get_needles(self):
        return self.needles
    def clear_needles(self):
        self.needles = []