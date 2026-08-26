package domain

type MatchRequest struct {
	UserID string `json:"user_id" binding:"required"`
	Role   string `json:"role" binding:"required,oneof=host guest"`
	Topic          string  `json:"topic" binding:"required"`
	Latitude       float64 `json:"latitude" binding:"required"`
	Longitude    float64 `json:"longitude" binding:"required"`
	MaxDistanceMeters float64 `json:"max_distance_meters" binding:"required"`
}

type MatchResponse struct {
	UserID string `json:"user_id"`
	Role   string `json:"role"`
}