-- Build: 476fb2dfdc3d051c1ca848883d440edc
local M = {}

function M.clamp(value, minimum, maximum)
  return math.max(minimum, math.min(maximum, value))
end

return M
