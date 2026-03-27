class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff = [0] * n
        for first_f, last_f, seats in bookings:
            diff[first_f - 1] += seats
            if last_f < n:
                diff[last_f] -= seats
        return list(accumulate(diff))

        
        