// $Id: line.cpp 1734 2018-01-05 09:39:04Z eyaker $

// Copyright (c)  2011, Norwegian Computing Center
// All rights reserved.
// Redistribution and use in source and binary forms, with or without modification,
// are permitted provided that the following conditions are met:
// •  Redistributions of source code must retain the above copyright notice, this
//    list of conditions and the following disclaimer.
// •  Redistributions in binary form must reproduce the above copyright notice, this list of
//    conditions and the following disclaimer in the documentation and/or other materials
//    provided with the distribution.
// THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY
// EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
// OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT
// SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
// SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT
// OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
// HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
// OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
// EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

#include "line.hpp"
#include "point.hpp"
#include <cassert>
#include <cmath>
#include <limits>

using namespace NRLib;

const double Line::min_ = 0.000001;

Line::Line()
  : p1_(0.0, 0.0, 0.0),
    p2_(0.0, 0.0, 0.0),
    end1_(true),
    end2_(true)
{}


Line::Line(const Point& p1_in, const Point& p2_in, bool end1_in, bool end2_in)
{
  assert((end1_in && end2_in) || p1_in != p2_in);  // Don't allow rays or infinite lines with no direction.
  p1_   = p1_in;
  p2_   = p2_in;
  end1_ = end1_in;
  end2_ = end2_in;
}


void Line::SetPt(const Point& p1_in, const Point& p2_in, bool end1_in, bool end2_in)
{
  assert((end1_in && end2_in) || p1_in != p2_in); // Don't allow rays or infinite lines with no direction.
  p1_   = p1_in;
  p2_   = p2_in;
  end1_ = end1_in;
  end2_ = end2_in;
  return;
}

bool Line::GetPt1(Point& pt1) const
{
    pt1 = p1_;
    return end1_;
}


bool Line::GetPt2(Point& pt2) const
{
    pt2 = p2_;
    return end2_;
}


// Calc length of def.line when finite line
double Line::GetLength() const
{
  if ( end1_ && end2_ )   // both points are endpoints; finite line
    return ( ( p2_ - p1_ ).Norm() );
  else {
    if ( std::numeric_limits<double>::has_infinity )
      return(std::numeric_limits<double>::infinity());
    else
      return std::numeric_limits<double>::max();
  }
}


// Calc shortest distance from p_in to def.line (or extention of finite line) at proj_pt
double Line::FindDistance(const Point& p_in) const
{
  Point proj_pt = FindProjection(p_in);
  return p_in.GetDistance(proj_pt);
}

// Calc shortest distance from p_in to def.line (or extension of line) at proj_pt
double Line::FindDistanceAndSide(const Point& p_in, bool& right_side) const
{
  Point  proj_pt   = FindProjection(p_in);
  Point  side_vec  = p_in - proj_pt;
  Point  line_vec  = p2_  - proj_pt;
  Point  cross     = side_vec.Cross(line_vec);
  if (cross.z >= 0) //true also if it is exact on line
    right_side = true;
  else
    right_side = false;
  return p_in.GetDistance(proj_pt);
}


// Calc projection_point on def.line from p_in (or extension of line when proj.pt from p_in is outside and line is not finite)
Point Line::FindProjection(const Point& p_in) const
{
  double diff_12 = p1_.GetDistance( p2_ );  // length of def.line
  if ( diff_12 == 0.0 )                    // if zero-length, returns p1 (=p2)
    return p1_;
  else {
    Point delta_p = p2_ - p1_;
    double t = delta_p.Dot( p_in - p1_ ) / ( diff_12*diff_12 );
    if ( t < 0.0 && end1_ )
      return p1_;
    else if ( t > 1.0 && end2_ )
      return p2_;
    return ( p1_ + t*delta_p );              // returns proj_pt for any t-value
  }
}

double Line::FindParameter(const Point& p_in) const
{
  double diff_12 = p1_.GetDistance( p2_ );  // length of def.line
  Point delta_p = p2_ - p1_;
  double t = delta_p.Dot( p_in - p1_ ) / ( diff_12*diff_12 );
  return t;
}

// Returns true if p_in is on the def.line, i.e. shortest distance to line (or extension) is less than min_in/0.0
bool Line::IsPointOnLine(const Point& p_in, double min_in) const
{
  if (FindDistance(p_in) < min_in )
    return true;
  else
    return false;
}


bool Line::IsParallel(const Line& line_in, double min_in) const
{
  if (Cross(GetDir(), line_in.GetDir()).Norm() < min_in) // true -> parallel
    return true;
  else
    return false;
}


// Based on example from softsurfer.com:
// http://softsurfer.com/Archive/algorithm_0106/algorithm_0106.htm
double Line::FindDistance(const Line   & line_in,
                          NRLib::Point & this_line_point,
                          NRLib::Point & in_line_point) const
{
  Point u   = GetPt2() - GetPt1();
  Point v   = line_in.GetPt2() - line_in.GetPt1();
  Point w   = GetPt1() - line_in.GetPt1();
  double a  = Dot(u, u);   // always > 0
  double b  = Dot(u, v);
  double c  = Dot(v, v);   // always > 0
  double d  = Dot(u, w);
  double e  = Dot(v, w);
  double dd = a*c - b*b;   // always > 0
  double sc, sn, sd = dd;   // sc = sn / sd
  double tc, tn, td = dd;   // sc = sn / sd

  // Nearest points:  s1 = p1_ + sc*u  and s2 = line_in.p1_ + tc*v.

  if (dd == 0) { // lines are parallel
    sn = 0;     // We use p1_.
    sd = 1;     // Don't divide on 0.
    tn = e;
    td = c;
  }
  else {
    sn = b*e - c*d;
    tn = a*e - b*d;
    if (IsEndPt1() && sn < 0) {
      sn = 0;
      tn = e;
      td = c;
    }
    else if (IsEndPt2() && sn > sd) {
      sn = sd;
      tn = e + b;
      td = c;
    }
  }

  if (line_in.IsEndPt1() && tn < 0) {
    tn = 0;
    // recalculate sc:
    if (IsEndPt1() && -d < 0) {
      sn = 0;
    }
    else if (IsEndPt2() && -d > a) {
      sn = sd;
    }
    else {
      sn = -d;
      sd = a;
    }
  }
  else if (line_in.IsEndPt2() && tn > td) {
    tn = td;
    // recalculate sc:
    if (IsEndPt1() && (-d + b) < 0) {
      sn = 0;
    }
    else if (IsEndPt2() && (-d + b) > a) {
      sn = sd;
    }
    else {
      sn = -d + b;
      sd = a;
    }
  }

  sc = (sn == 0.0 ? 0.0 : sn / sd);
  tc = (tn == 0.0 ? 0.0 : tn / td);

  this_line_point = GetPt1() + sc*u;
  in_line_point = line_in.GetPt1() + tc*v;

  return Norm(this_line_point - in_line_point);
}


bool Line::IsOverLapping(const Line& line_in, double min_in) const
{
  if (!IsParallel(line_in, min_in))  // must be parallel for overlapping
    return false;      // not overlapping
  else   {
    if (IsPointOnLine(line_in.GetPt1(), min_in))
      return true;
    else if (IsPointOnLine(line_in.GetPt2(), min_in))
      return true;
    else if (line_in.IsPointOnLine(p1_, min_in))
      return true;
    else if (line_in.IsPointOnLine(p2_, min_in))
      return true;
    else
      return false;    // not overlapping
  }
}

bool Line::IntersectXY(const Line & line_in, Point & intersect_pt, const bool& infinite) const
{
  bool is_intersect = false;
  intersect_pt = Point(0.0, 0.0, 0.0);

  //def. line on general form a1*x + b1*y = c1
  const double a1 = p1_.y - p2_.y;
  const double b1 = p2_.x - p1_.x;
  const double c1 = p1_.y*p2_.x - p2_.y*p1_.x;

  //line_in on general form a2*x + b2*y = c2
  Point p1_in = line_in.GetPt1();
  Point p2_in = line_in.GetPt2();
  const double a2 = p1_in.y - p2_in.y;
  const double b2 = p2_in.x - p1_in.x;
  const double c2 = p1_in.y*p2_in.x - p2_in.y*p1_in.x;

  double den = a1*b2 - b1*a2;
  if(den != 0)
  {
    double x = (c1*b2 - b1*c2) / den;
    double y = (a1*c2 - c1*a2) / den;
    Point tmp(x, y, 0.0);
    if (!infinite)
    {
      Line line_xy = LineXY();                  //Must project to xy-plane before finding parameter
      Line line_in_xy = line_in.LineXY();
      double t1 = line_xy.FindParameter(tmp);
      double t2 = line_in_xy.FindParameter(tmp);
      if (t1 <= 1.0 && t1 >= 0.0 && t2 <= 1.0 && t2 >= 0.0)
      {
        intersect_pt = tmp;
        is_intersect = true;
      }
    }
    else
    {
      Line line_in_xy = line_in.LineXY();
      double t_in = line_in_xy.FindParameter(tmp);
      if (t_in <= 1.0 && t_in >= 0.0)
      {
        intersect_pt = tmp;
        is_intersect = true;
      }
    }
  }
  return is_intersect;
}

Line Line::LineXY() const
{
  Point p1 = p1_;
  Point p2 = p2_;
  p1.z = 0;
  p2.z = 0;
  Line line_xy(p1, p2, end1_, end2_);
  return line_xy;
}
