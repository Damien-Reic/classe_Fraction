using System;

public class Fraction
{
    private int _num;
    private int _denom;

    public Fraction(int num, int denom = 1)
    {
        if (denom < 0)
        {
            num = -num;
            denom = -denom;
        }

        int pgdc = GetPgdc(num, denom);
        _num = num / pgdc;
        _denom = denom / pgdc;
    }

    public override string ToString()
    {
        if (_denom == 1)
        {
            return _num.ToString();
        }
        else
        {
            return $"{_num}/{_denom}";
        }
    }

    public string ToStr()
    {
        return $"({_num}/{_denom})";
    }

    public bool Equals(Fraction autre)
    {
        if (autre is Fraction)
        {
            return _num == autre._num && _denom == autre._denom;
        }
        else if (autre is int || autre is float)
        {
            return Equals(new Fraction((int)autre));
        }
        else
        {
            throw new Exception($"{autre.GetType()} n'est pas supporté");
        }
    }

    public bool LessThan(Fraction autre)
    {
        if (autre is Fraction)
        {
            return _num * autre._denom < autre._num * _denom;
        }
        else if (autre is int || autre is float)
        {
            return LessThan(new Fraction((int)autre));
        }
        else
        {
            throw new Exception($"{autre.GetType()} n'est pas supporté");
        }
    }

    public bool GreaterThan(Fraction autre)
    {
        if (autre is Fraction)
        {
            return _num * autre._denom > autre._num * _denom;
        }
        else if (autre is int || autre is float)
        {
            return GreaterThan(new Fraction((int)autre));
        }
        else
        {
            throw new Exception($"{autre.GetType()} n'est pas supporté");
        }
    }

    public static explicit operator int(Fraction fraction)
    {
        return fraction._num / fraction._denom;
    }

    public static explicit operator float(Fraction fraction)
    {
        return (float)fraction._num / fraction._denom;
    }

    public Fraction Abs()
    {
        return new Fraction(Math.Abs(_num), Math.Abs(_denom));
    }

    public Fraction Neg()
    {
        return new Fraction(-_num, _denom);
    }

    public Fraction Add(Fraction autre)
    {
        if (autre is Fraction)
        {
            return new Fraction((_num * autre._denom) + (autre._num * _denom), _denom * autre._denom);
        }
        else if (autre is int || autre is float)
        {
            return Add(new Fraction((int)autre));
        }
        else
        {
            throw new Exception($"{autre.GetType()} n'est pas supporté");
        }
    }

    public Fraction Subtract(Fraction autre)
    {
        if (autre is Fraction)
        {
            return new Fraction((_num * autre._denom) - (autre._num * _denom), _denom * autre._denom);
        }
        else if (autre is int || autre is float)
        {
            return Subtract(new Fraction((int)autre));
        }
        else
        {
            throw new Exception($"{autre.GetType()} n'est pas supporté");
        }
    }

    public Fraction Multiply(Fraction autre)
    {
        if (autre is Fraction)
        {
            return new Fraction(_num * autre._num, _denom * autre._denom);
        }
        else if (autre is int || autre is float)
        {
            return Multiply(new Fraction((int)autre));
        }
        else
        {
            throw new Exception($"{autre.GetType()} n'est pas supporté");
        }
    }

    public Fraction Divide(Fraction autre)
    {
        if (autre is Fraction)
        {
            return Multiply(new Fraction(autre._denom, autre._num));
        }
        else if (autre is int || autre is float)
        {
            return Divide(new Fraction((int)autre));
        }
        else
        {
            throw new Exception($"{autre.GetType()} n'est pas supporté");
        }
    }

    public Fraction Power(int autre)
    {
        if (autre < 0)
        {
            return new Fraction((int)Math.Pow(_denom, Math.Abs(autre)), (int)Math.Pow(_num, Math.Abs(autre)));
        }
        else
        {
            return new Fraction((int)Math.Pow(_num, autre), (int)Math.Pow(_denom, autre));
        }
    }

    public float ToDecimal()
    {
        return (float)_num / _denom;
    }

    public Fraction Invert()
    {
        return new Fraction(_denom, _num);
    }

    public Fraction Simplify()
    {
        return new Fraction(_num, _denom);
    }

    public int GetNum()
    {
        return _num;
    }

    public int GetDenom()
    {
        return _denom;
    }

    public static int GetPgdc(int num, int denom)
    {
        if (num is int && denom is int)
        {
            if (num == 0 || denom == 0)
            {
                return num > 0 ? num : 1;
            }
            if (num < 0 || denom < 0)
            {
                return GetPgdc(num: Math.Abs(num), denom: Math.Abs(denom));
            }
            if (denom != 0)
            {
                return GetPgdc(num: denom, denom: num % denom);
            }
        }
        throw new Exception("Invalid type for the get_pgdc arguments");
    }
}

public class Program
{
    public static void Main(string[] args)
    {
        Fraction frac = new Fraction(1, 2);
        Fraction frac2 = new Fraction(1,2);
        Console.WriteLine(frac.ToString());
        Console.WriteLine(frac.ToString() == frac2.ToString());
    }
}
