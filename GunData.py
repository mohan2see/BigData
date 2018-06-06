from mrjob.job import MRJob
from mrjob.step import MRStep
import sys

class RatingsBreakDown(MRJob):
	def steps(self):
		return [
				MRStep(mapper=self.mapper_get_ratings,
					   reducer=self.reducer_count_ratings),
				MRStep(reducer=self.reducer_sorted_output)
		]

	def mapper_get_ratings(self, _, line):
		(state,killed) = line.split(',')
		yield state,killed

	def reducer_count_ratings(self, state, killed):
		killed_list = list(killed)
		yield killed_list,state

	def reducer_sorted_output(self, count, movies):
		y=0
		county=0
		for j in movies:
			for i in count:
				county=int(count[y])+county
				y=y+1
			yield j,county
			

if __name__ == '__main__':
	RatingsBreakDown.run()