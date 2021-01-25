
from controllers import *
route = [
		(
			r"/shutdown",
			home.BlackOutHandler
		)
		,(
			r"/cancel",
			home.CancelBlackOutHandler
		)
]
					